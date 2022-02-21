# My first postmortem

### resumen:

**On January 21, 2022 at 3:00 pm** users experienced a server problem which yielded an error status of **500 (internal server error)**. The root cause of the error was a single letter typo in which a **.php** file was written as a **.phpp**.

### Timeline:

**3:00 pm: **after deploying a WordPress update, an engineer noticed that the website was not loading and then checking the status of the request noticed that it was throwing a 500 error.

**3:05 pm: **All running processes on a particular server were checked using `ps auxf`. The apache2 and MySQL database processes were found to be running as expected, indicating that the error was localized to the WordPress implementation.

**6:00 pm:** Edited the WordPress file `/var/www/html/wp-config.php` to enable WordPress debug mode.

**6:34 pm:** Found the error in a WordPress configuration file `/var/www/html/wp-settings.php`. It turns out that the error was a typo when importing a required `/var/www/html/wp-includes/class-wp-locale.phpp` file. The **.phpp** extension indicated a possible typo.

**6:40 pm:** Fixed the typo on the individual server using` sed -i 's/phpp/php/' /var/www/html/wp-settings.php`.

**6:41 pm:** website service was tested once again and content was served as expected.

**6:42 pm:** A puppet manifest was developed to fix this problem on a large scale.

**6:45 pm:** The puppet manifest was deployed to all remaining servers, which returned the website service to 100%.

### Root Cause and Resolution:

The root cause of this outage was a typo in the php file **/var/www/html/wp-settings.php** in which required the `/var/www/html/wp-includes/class-wp-locale.phpp` file. The extension of **.phpp** was a typo, intended to be **.php**. Since `/var/www/html/wp-includes/class-wp-locale.phpp` did not exist and was required, a fatal error was generated that prevented the content from being served. Since this code was implemented on all servers, this error caused a 100% outage. A puppet manifest was developed and implemented to correct the typo on all servers, restoring service within 12 minutes of the outage.

### Corrective and preventative measures:

To prevent large-scale problems like this from occurring in the future, code should never be deployed to all servers prior to testing. Some things to consider for the future are: developing an enterprise-wide test protocol, setting up isolated docker containers for testing purposes, and implementing a two-person sign-off before a major deployment.
