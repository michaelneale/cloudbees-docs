.. _sdk:

=========================
 CloudBees SDK
=========================

.. highlight:: bash

The CloudBees SDK provides a convenient command line interface for managing your CloudBees account
using the CloudBees API.

Note on running applications in European region
-----------------------------------------------

Note, if you are dealing with applications in the European cloudbees data centre, you can use the flag "-ep eu" flag to tell it to run the command in europe for any of the commands below. If you are often performing actions against the EU region, we recommend you set the api endpoint in the "bees.config" file (~/.bees/bees.config) to be: bees.api.url=https\://api-eu.cloudbees.com/api - to ensure you are always talking to the EU region.

Prerequisites
-------------

Java 6 or greater must be installed and the java command must be available on the PATH (verify by running: java -version)


Download and configure
----------------------

Download the CloudBees SDK and unzip it into a directory on your machine (we'll refer to as BEES_HOME from now on)

To run the CloudBees command line tools, you need to set the BEES_HOME environment variable, and add BEES_HOME to your PATH environment variable.

The first time you run the bees command, you will be prompted to enter your CloudBees email address and password, your API keys will then be cached in your USER_HOME/.bees/bees.config file so that you won't need to enter them for any of the commands.

Installation for OSX and Linux
------------------------------

Open a command-line console (launch the Terminal application on OSX) and then download SDK zip file and install unzip it into a directory. ::

   $ curl -L cloudbees-downloads.s3.amazonaws.com/sdk/cloudbees-sdk-1.2.2-bin.zip > bees_sdk.zip
   $ unzip bees_sdk.zip
   $ rm bees_sdk.zip
   $ cd cloudbees-sdk-1.2.2

Add the bees variables to your OS-X/linux command line environment by adding the following lines to your /.bash_profile or /.profile file (you may need to create this file) ::

   $ export BEES_HOME=~/cloudbees-sdk-1.2.2
   $ export PATH=$PATH:$BEES_HOME

Refresh your terminal's bash session by executing ::

   $ source /.bash_profile #(or /.profile as the case may be)

Alternate Installation for OSX
------------------------------

If you have the homebrew package manager, then simply run ::

   $ brew install cloudbees-sdk

Installation for Windows
------------------------

On Windows, you can open a predefined Bees Console window by double clicking on the BEES_HOME\Bees Console icon. Please avoid a path with spaces in it in your installation directory ! (eg don't use Program Files if you can avoid it). 

Running behind a proxy
----------------------

If you are running the SDK commands on a machine that is behind a proxy, you may receive "Connection timed out" errors. The SDK supports a full set of proxy parameters:


