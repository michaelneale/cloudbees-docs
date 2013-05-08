.. _tomcat-stack:

================================
 Tomcat
================================

.. contents::
    :local:
    :depth: 1

Tomcat is the most popular Servlet container for deploying Java-based Web
applications.

You can deploy your applications on Apache Tomcat 7 using the tomcat7 stack ID.

.. code-block:: bash

   bees app:deploy -t tomcat7 WAR_FILE


Tomcat7 is currently classified as a "Managed" stack, which means that it
supports a subset of the features provided by a "curated" stack.  If you are
looking for a curated Tomcat stack, you can use the standard CloudBees
:ref:`tomcat <tomcat6>` stack.


Features
--------

============================  ============================================
Feature                       Notes
============================  ============================================
Runtime version               Apache Tomcat 7.0.39
App package formats           WAR files
Resource injections           As system properties
Datasources                   Manual (via context.xml)
App Parameters                As system properties
Stats monitoring              Process level only
Static Scaling                Supports horizontal and vertical
Auto-scaling                  Not supported
Monitoring                    New Relic, AppDynamics
Logging                       Standard, Papertrail
============================  ============================================

See the `clickstack repository <https://github.com/CloudBees-community/tomcat7-clickstack/>`_
for info about planned features.


Runtime Parameters
------------------

You can customize the stack by applying runtime parameters using the options
provided by the :ref:`sdk`.

============================  ============================================
Runtime parameter             Description
============================  ============================================
JAVA_OPTS                     Java args added to the command line
java_version                  Java version to be used (1.6, 1.7 or 1.8)
============================  ============================================

Examples:

.. code-block:: bash

   bees config:set -a APP_ID -RJAVA_OPTS=-Dname=value

.. code-block:: bash

   bees app:deploy -a APP_ID -Rjava_version=1.7 WAR_FILE

Application Parameters
----------------------

Application parameters are exposed by this stack as System Properties.

Examples:

.. code-block:: bash

   bees config:set -a APP_ID myAppParam=myValue

.. code-block:: bash

   bees app:deploy -a APP_ID -PmyAppParam=myValue

These application parameters can be used by your application using the following
code snippet:

.. code-block:: java

   String param = System.getProperty("myAppParam");


Resource Bindings
-----------------

Resources may be bound to your applications provided by the standard
:ref:`resource binding <app-resources>` mechanisms.

.. code-block:: bash

   bees app:bind -a APPID -r RESOURCE_ID -as ALIAS

Resource bindings are available to applications as system properties formed
in the following way:  <RESOURCE-TYPE>_<ALIAS>_<KEY>

Each resource type provides a different set of keys, so you be sure to read the
documentation for the resource type you are trying to use.

Database Bindings
-----------------

CloudBees MySQL Databases are a commonly used resource type that that can be
easily bound to your application using the following SDK command:

.. code-block:: bash

   $ bees app:bind -a APPID -db DATABASE_NAME -as ALIAS

\-a APPID
   the ID of your application (formatted: ACCOUNT/APPNAME)
-db DATABASE_NAME
   the name of your CloudBees MySQL database
-as ALIAS
   the name of the binding which is used to identify the binding and to compose
   the name of the environment variables used to describe this binding.

Database parameters via System Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tomcat7 Databases bound to your are not (yet!) automatically injected into the
app container's JNDI namespace, but they are available as System properties as
described above.  So in the following example:

.. code-block:: bash

   $ bees db:create db123
   $ bees app:bind -a myaccount/myapp -db db123 -as mydb

The above commands will create a database and bind it to the application.  The
binding will trigger the injection of the following System Properties:

DATABASE_URL_MYDB
   url of the database starting with "mysql:"
   (e.g. "mysql://ec2-1.2.3.4.compute-1.amazonaws.com:3306/my-db"). Please note
   that this URL is not prefixed by "jdbc:".
DATABASE_USERNAME_MYDB
   username of the database
DATABASE_PASSWORD_MYDB
   password of the database

Configuring Tomcat to use a Database binding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In your war application, declare a standard `Tomcat JNDI DataSource <https://github.com/CloudBees-community/tomcat7-clickstack/>`_
in a "META-INF/context.xml" file using Tomcat variable substitution syntax
${propname} to inject your binding parameters.

.. code-block:: xml

   <Context>
      <Resource
           name="jdbc/my-db"
           auth="Container"
           type="javax.sql.DataSource"

           url="jdbc:${DATABASE_URL_MY_DB}"
           username="${DATABASE_USERNAME_MY_DB}"
           password="${DATABASE_PASSWORD_MY_DB}"

           driverClassName="com.mysql.jdbc.Driver"

           maxActive="20"
           maxIdle="1"
           maxWait="10000"
           removeAbandoned="true"
           removeAbandonedTimeout="60"
           logAbandoned="true"

           validationQuery="SELECT 1"
           testOnBorrow="true"
           />
   </Context>

Your database will now be accessible as a JNDI datasource named
"java:comp/env/jdbc/mydb".

Code sample

.. code-block:: java

   Context ctx = new InitialContext();
   DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/my-db");
   Connection conn = ds.getConnection();
   ResultSet rst = stmt.executeQuery("select 1");
   while (rst.next()) {
     out.print("resultset result: " + rst.getString(1));
   }
   rst.close();
   stmt.close();
   conn.close();

Application Logging
-------------------

System out and err output from application processes are captured in a log file
that can be viewed from the logs tab of your app in the RUN@cloud web console
or via the Bees SDK app:tail command.  To generate content to this log, you
need to use System.out stream or you can configure your logging framework to
output to the System streams.

Log files are not permanently stored and will be lost when your application
instance is replaced or destroyed.  To consolidate and permanently store
application logs, you can configure your app to send log data to Papertrail.
`Papertrail <https://grandcentral.cloudbees.com/services/plans/papertrail>`_
provides a very powerful logging service that lets you store, search,
your logs and to trigger alerts based on content in your logs.

If your application generates its own log files outside of the System.out
stream, you will need to create your own mechanisms for managing log size and
ways to gather and view your logs.

Troubleshooting Errors
----------------------

OutOfMemoryExceptions
^^^^^^^^^^^^^^^^^^^^^

Untuned, long running applications commonly encounter OutOfMemoryExceptions that
can cause applications to stop responding to requests.  While this problem is
clearly an application error, this stack will detect OutOfMemoryExceptions
thrown by applications and automatically trigger a restart of the application.

While this approach allows applications to quickly recover from internal
application errors, it indicates an unstable application behavior that should
be investigated by the application developers.  OutOfMemory restarts are
typically visible in your application logs, which can be used to investigate
the cause of these errors more deeply.

java.lang.OutOfMemoryError: PermGen space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Having an OutOfMemoryError in your log is a sign that your application might
need more PermGen space.  You can use the following command to change your
permgen size:

.. code-block:: bash

   bees app:update acme/test jvmPermSize=256


502 Unavailable Errors
^^^^^^^^^^^^^^^^^^^^^^

502 errors are reported by the application routing layer when all
application instances are not responding to incoming requests. Common causes
of 502 errors are:

* The app hung or crashed during startup and never started receiving requests
* All app threads are making external connnections - this can occur if the application makes blocking requests to external servers (databases, HTTP URLs, or other external resources) that are not responding properly
* App threads are stuck in synchronization or object lock deadlocks
* The apps process has crashed and is not responding to requests

In almost all of these cases, the application logs are the best source of info
about this error.  If you have paid for production support or need to post
a question on the community forums, error messages and stack traces are by
far this most useful piece of information that you can provide to get help.


Collecting Stack Dumps
^^^^^^^^^^^^^^^^^^^^^^

If your application is still running, but not responding, you can capture stack
dump via the following command:

.. code-block:: bash

   $ bees app:instance:list acme/myapp
   Instance ID     : acme/iii-aaa
   $ bees app:instance:invoke -i acme/iii-aaa -cs send_sigquit

After invoking send_sigquit, the stack dump will be dumped to the application
log of the instance.  You can view this dump in the log viewer or via the
bees app:tail command.

.. code-block:: bash

   $ bees app:tail acme/myapp



Frequently Asked Questions
==========================

How can I determine the web application root directory?
   use ServletContext.getRealPath("/")

Where can I store temporary files?
   Use File.createTempFile(tempFileName)
   or ServletContext.getAttribute("javax.servlet.context.tempdir")

Does this stack support persistent file storage?
   Yes, via a mounted filestore resource

What is the default timezone?
   UTC

How can I override the timezone?
   In general, this is a bad practice since keeping everything UTC helps prevent
   timezone corruption.  You can override the timezone using a runtime parameter
   to set -Duser.timezone=YOUR_TIME_ZONE






