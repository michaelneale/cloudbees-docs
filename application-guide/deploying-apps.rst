.. _deploying-apps:

================================
 Deploying Applications
================================

.. contents::
    :local:
    :depth: 1

.. sidebar:: Basic Steps to deploy an app

    - Subscribe to the Application Service
    - Install the :ref:`sdk`
    - Create an application package
    - Deploy using *bees app:deploy*

*Deploying* is the process of sending your packaged application binary
(a.k.a application package) to CloudBees to run it.

A Trivial Deployment Example 
----------------------------

The most basic example of deploying an app to Cloudbees is to zip up a webapp
directory structure (with some static HTML files in it) and deploy it using
the following commands:

.. code-block:: bash

   $ zip /Home/myappdir myapp.zip

   $ bees app:deploy --appid myapp myapp.zip
   Deploying application: acme/myapp
   Uploading application deltas ...
   ........................uploaded 25%
   ........................uploaded 50%
   ........................uploaded 75%
   ........................upload completed
   deploying application to server(s)...
   Application acme/myapp deployed: http://myapp.acme.cloudbees.net

After the command completes, the files from /Home/myappdir will be available
from the URL that was automatically created for your application.

What just happened?
^^^^^^^^^^^^^^^^^^^

Here's a quick examination of the gory details performed by those commands...

* By zipping up a directory, you created an "application package" that can be
  deployed to an application container on CloudBees.
* The bees app:deploy command uploaded the myapp.zip file to the CloudBees API
  endpoint and told it to deploy the app package using the App ID 'myapp' (the
  ID can later be used to update the same application with a new package).
* Since CloudBees did not have an application matching the ID 'myapp' on the
  *acme* account, a new application was created using the default configuration.
  The default configuration provided the selection of the default 'tomcat'
  container type and the myapp.acme.cloudbees.net hostname.
* CloudBees searched the global server pool for a space to launch a new application
  container for the application.
* The deployed application package was sent to the CloudBees server, the app
  process was launched using the supplied package.
* The CloudBees HTTP routing layer was updated to direct incoming requests for
  the app's hostname to the running application instance.

Stacks and Packages
-------------------

To deploy an application, you will need to review the list of available
:ref:`Application Stacks <clickstacks>` and the application package formats
that are accepted for the stack you are deploying to.

Package format examples:

* Java web applications typically run in application containers that support
  the Servlet Web Archive (WAR) format. The WAR file format requires the
  application to compiled into .class files which are then packaged inside the
  WAR file (which is just a ZIP file with a .war extension).
* PHP, Python and Ruby applications typically run as open directory structures
  with the raw source files sitting in the directory, so to deploy them you
  will use a standard ZIP file. 

Deploying with CloudBees SDK
----------------------------

The :ref:`CloudBees SDK <sdk>` provides you with command-line utilities for
deploying your applications.

Use -a to set the ID of the application you are deploying.

.. code-block:: bash

   $ bees app:deploy -a APP_ID APP_PACKAGE_PATH

Use -t to specify the :ref:`Application Stack <clickstacks>`.

.. code-block:: bash

   $ bees app:deploy -a APP_ID -t STACK_ID APP_PACKAGE_PATH

Use -P to set :ref:`configuration parameters <app-config-params>` that can be
used by your application at runtime.

.. code-block:: bash

   $ bees app:deploy -a APP_ID APP_PACKAGE_PATH -P key=value

Uploading from a Web Browser
----------------------------
The CloudBees Web Console lets you to deploy applications directly from your
browser.

* Open the RUN@cloud Web Console
* Use the *Create Application* form to create an empty application
* After the new app's configuration page open, click the 'Upload a file' button
* Enter the path to the local application package you want to upload
* Click finish

TODO: change the upload button to say 'Upload a file'
TODO: add a screenshot

Deploying with Eclipse
----------------------

Install the :ref:`eclipse-toolkit` to add capabilities for deploying
applications directly from your Eclipse IDE.

**Deploy from CloudBees-enabled Projects**

* Right-click on the project
* Select: Run As > CloudBees Application (RUN@cloud)
* Enter an App ID if prompted

**Non-native CloudBees Project**

* Trigger a project build that will generate an application package (typically
  a .war file)
* right-click on the application package and choose the CloudBees deploy command

TODO: add some screenshots

Continuous Deployment with Jenkins
----------------------------------

If you have Jenkins build jobs that are producing application artifacts that
can be run in a CloudBees app container, then you can use the
:ref:`cloudbees-deployer` to deploy your artifacts at the end of your Jenkins
build jobs.  This lets you to automatically build, test and deploy your
applications whenever developers commit code changes (we call this
continuous deployment!).

* Open the configuration page for your Jenkins build job.  Make sure this job
  is setup to produce an artifact that matches the application package format
  supported by your application stack (ex: WAR files for Java Web apps).
* Scroll down to the  post-build actions and click 'Add post-build action'
* Select the 'Deploy to CloudBees' option
* Click the 'Add Web Application > First match' option
* Enter the Application ID you want to deploy with
* Enter the path to a WAR file
* Save the configuration

Future builds will now deploy the application artifact if the build
successfully passes all compilation and tests.


