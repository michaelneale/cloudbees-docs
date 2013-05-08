.. _clickstacks:

========================
 Application Stacks
========================

The CloudBees ClickStack architecture is the core foundation that allows
developers to choose from a variety of runtimes for running their applications.

Choosing a Stack
----------------

All applications deployed to RUN@cloud are associated with an application runtime container type (also known as a Stack or ClickStack).  By default, applications are setup to use a simple web container based on Tomcat 6.  The type can be overriden via the -t argument in the CloudBees SDK's deploy command:

.. code-block:: bash

   $ bees app:deploy -a APPID -t STACK_ID PATH_TO_WAR_FILE

.. _java-stacks:

Java Stacks
-----------

.. toctree::
    :maxdepth: 1

    tomcat-stack
    jboss-stack
    java-stack

CloudBees currently offers three curated application stacks for running
Java applications.

+--------------+----------------------------------+--------------+-----------------------+
| Stack ID     | Description                      | Application  | More Info             |
|              |                                  | Format       |                       |
+==============+==================================+==============+=======================+
| tomcat       | Servlet application container    | Servlet WAR  | :ref:`Learn more      |
|              | based on Tomcat 6.0.32. This     | File (.war)  | <tomcat-stack>`       |            
|              | is the default container type.   |              |                       |
+--------------+----------------------------------+--------------+-----------------------+
| jboss        | Java EE 6 Web Profile            | Servlet WAR  | :ref:`Learn more      |
|              | container based on JBoss 7.02    | File (.war)  | <jboss-stack>`        |
|              |                                  |              |                       |
+--------------+----------------------------------+--------------+-----------------------+
| java         | Executes Java applications that  | JAR or ZIP'd | :ref:`Learn more      |
|              | are launched via Class.main()    | directory    | <java-stack>`         |
|              |                                  |              |                       |
+--------------+----------------------------------+--------------+-----------------------+

Community Stacks
------------------------

.. toctree::
    :maxdepth: 1

    nodejs-stack
    php-stack
    ruby-stack





