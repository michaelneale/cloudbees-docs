.. _entrprise-data:

================================
 Enterprise Data Access
================================

.. contents::
    :local:
    :depth: 1

While moving applications 100% to the Cloud is a noble goal, there are often cases where an application needs to connect back to resources in the private corporate network, which is typically secured by a firewall or VPN.

This article explores some of the approaches that you may consider when designing an app that needs to connect to servers deployed in other networks.

Direct connections
==================

The easiest (and least secure) way to connect to corporate servers is to make sure that the target server is publicly accessible for connections from remote Internet clients, and then use authenticated (and preferably encrypted) protocols for establishing connections to those servers.  You will then be able to connect to your corporate server using an appropriate client embedded into the application.  To store the secure credentials that your application will use to establish a connection with the corporate server, consider using Application Configuration Parameters which will be made available to your application at runtime.

Steps to setup:

* Determine the hostname of the corporate resource that you will be connecting to.  Make sure this is publicly accessible.
* Embed a client library in your application that is capable of connecting to this server.  For example, if this is a Database, you'll need a JDBC driver
* Write the code to establish a connection to your server using the client library

Corporate Database <-- CloudBees Application

Firewalled Configurations
=========================

For obvious security reasons, it is very common for IT environments to disallow direct Internet connections to key servers like databases or other backend systems with critical backend.  To prevent access to these servers, the corporate network is often protected by a firewall that tightly controls who and what can communicate through the firewall.

Here are various options available for connecting to your protected corporate resources through a firewall:

Dedicated Application IPs
-------------------------

CloudBees offers the ability to setup dedicated servers on your account to improve security isolation and provide more consistent performance.  You can additionally purchase a static IP address for your servers so that connections made from apps deployed on the server will have a well-known IP address.  This allows you provide your corporate IT team with a set of IP addresses that can be whitelisted for connecting to your corporate network through the firewall.

Steps to setup:

* Contact CloudBees Sales to add to a dedicated server with a fixed IP address
* Configure your corporate firewall to allow connections from the IP address assigned to your Dedicated Server
* Associate your CloudBees application with the new dedicated server pool so that deployments of the app will always land on the server.

At this point, connections from your application will be associated with an IP address approved by your firewall, so you should be able to connect to your corporate resources.

Firewall(Corporate Database) <-- CloudBeesDedicatedServer(CloudBees Application)

Application Gateway
-------------------

Rather connecting directly to the database, you may consider setting a custom application gateway that has privileged access to your corporate network and is itself publicly accessible. This is commonly referred to as a DMZ (http://en.wikipedia.org/wiki/DMZ_%28computing%29) architecture.  This allows you to keep your backend corporate servers secured while allowing you to tightly control the interfaces that can be used by your CloudBees applications to read and/or write data from your backend systems.  In the configuration, you'll probably want to expose web-service APIs on your gateway application that is running in the DMZ that can be used by your CloudBees applications.

Steps to setup:

* Design and build an IT application (the Gateway) that exposes high-level interfaces via a secure protocol (like HTTPS) for interacting your backend systems.
* Deploy the Gateway app in your corporate DMZ environment with a publicly accessible hostname.  (Note this will not be a CloudBees managed application, you will need to maintain this like any other internal IT application).
* Write code in your CloudBees application that securely connects to your Gateway app


Firewall(Corporate Database) <-- Application Gateway <-- CloudBees Application

VPN Gateway
-----------

Some corporate networks allow you to gain access to the private network using a VPN client.    Since VPN clients typically need to be installed directly on a server and affect low level network configuration, it is not possible to establish a VPN connection directly from your applications deployed on CloudBees.  

Your best alternative establishing a native VPN connection from the app is to use a variant of the Application Gateway approach where you setup a custom server (that will be maintained external to CloudBees) that is configured to access your corporate network via VPN.   You can then design and deploy a secure gateway application on that server that can be used by your CloudBees application to communicate with resources on your private network.


Firewall(Corporate Database) <-- VPNClient(Application Gateway) <-- CloudBees Application

Virtual Private Cloud (VPC)
---------------------------

TODO: needs content
