.. _intro:

==========================
 Introduction to CloudBees
==========================

.. contents::
    :local:
    :depth: 1

What is CloudBees?
==================

CloudBees is a fully managed Platform as a Service that encompasses the
entire development, testing, staging, and production needs of application
developers and deployers

CloudBees provides a turnkey environment for deploying your Cloud-based
applications and a full-powered Jenkins-based continuous integration
solution for controlling how applications are built and tested.

What do I need?
===============

.. sidebar:: Helpful Tools
    :subtitle: These tools may be helpful to get started

    - :ref:`sdk`
    - :ref:`eclipse-toolkit`

*CloudBees* runs in the Cloud, so you don't need anything to get started,
but there are some tools that may be helpful for managing your account
or for using CloudBees in your day-to-day application development.

The CloudBees SDK provides a command line interface (CLI) that helps
you use the CloudBees API from your favorite command prompt.  The SDK
includes commands for managing your apps, databases, configuration and
bindings.

The CloudBees Eclipse Toolkit is a plugin for your Eclipse environment
that will expose many of the CloudBees management features directly in
the Eclipse IDE.  This includes functionality for creating application
projects and deploying applications.


Get Started
===========

If this is the first time you're trying to use CloudBees, then you should
read our getting started tutorials:

- :ref:`first-app-steps`
- :ref:`first-jenkins-steps`

How it works …
==============

.. topic:: \ 

    - **Deploy your applications**

        CloudBees is easy to use and manage, and it *doesn't require any servers*

        To deploy an app, you can just select a container, and upload an application
        package container. Here is an simple example of deploying an app with the
        optional CloudBees command line tools:

        .. code-block:: bash

            $ bees app:deploy -t tomcat --appid myapp myapp.war
            Deploying application: acme/myapp
            Uploading application deltas ...
            ........................uploaded 25%
            ........................uploaded 50%
            ........................uploaded 75%
            ........................upload completed
            deploying application to server(s)...
            Application acme/myapp deployed: http://myapp.acme.cloudbees.net

    - **Bind Ecosystem resources to applications**
        
        Use the CloudBees Ecosystem to create databases or other resources
        that can be used by applications to store data, send email, monitor
        performance and more....
        
    - **Use Jenkins to manage build jobs for your projects**

        The highly customizeable Jenkins continuous integration environment 
        lets you control the entire process for building and testing your
        application before it is tested.

        Jenkins provides hundreds of plugins to support building and testing
        virtually any project.

        Your applications's source code can live in the CloudBees GIT/SVN Forge, or
        you can use your existing source code repositories (including GitHub!).

        Take advantage of the CloudBees deployer to deploy your applications
        directly to the Cloud.

    - **Configure continuous deployment environments**

        Gain visibility about the quality of your applications at all times by
        setting up testing and staging environments that are always up-to-date
        with the latest code submitted by your developers.

        Define rules to control how incoming source code changes make their way
        through various environments.  Define quality checks along the way to
        ensure your applications behave as expected when code changes finally
        make it to your users.

        Leverage the CloudBees Deployer plugin for Jenkins to publish your applications
        directly to the Cloud.


