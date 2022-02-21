# My first postmortem

### Summary:

**on December 15, 2021 between 12pm and 5pm** between 12pm and 5pm the files sent were not sent correctly causing a status error **500(internal server error)**, what cause? there were several problems, but many were easy to solve, syntax errors in the code, indentation errors and a file had a small error in the extension instead of **php** the file was written as **pphp** it is thought it was a typo

### Timeline:

**between 12pm and 1pm: **after deploying a WordPress update, an engineer noticed some that there was a runtime issue, that the website was not loading, and then when checking the status of the request, he noticed which was throwing a 500 error.

**between 1pm and 3pm: **checking each file, we noticed syntax errors and fixed them immediately, once that was done, all processes running on a particular server were checked using `ps auxf `. The apache2 and MySQL database processes were found to be running as expected, indicating that the bug was localized to the WordPress implementation.

**a las 3:05pm:** Edited the WordPress file `/var/www/html/wp-config.php` to enable WordPress debug mode.

**3:50 pm:** Found the error in a WordPress configuration file `/var/www/html/wp-settings.php`. It turns out that the error was a typo when importing a required `/var/www/html/wp-includes/class-wp-locale.phpp` file. The **.phpp** extension indicated a possible typo.

**3:55 pm:** Fixed the typo on the individual server using` sed -i 's/phpp/php/' /var/www/html/wp-settings.php`.

**3:57 pm:** website service was tested once again and content was served as expected.

**3:59 pm:** A puppet manifest was developed to fix this problem on a large scale.

**4:05 pm:** The puppet manifest was deployed to all remaining servers, which returned the website service to 100%.

### Root Cause and Resolution:

The main cause of this outage was typos and syntax errors in the php file **/var/www/html/wp-settings.php** where `/var/www/html/wp-includes/class was required -wp-locale .phpp` file. The **.phpp** extension was a typo, meant to be **.php**. Since `/var/www/html/wp-includes/class-wp-locale.phpp` did not exist and was required, a fatal error was generated that prevented the content from being served. Since this code was deployed to all servers, this error caused a 100% outage. Developed and deployed a puppet manifest to fix the typo on all servers, restoring service within 13 minutes of outage.

### Corrective and preventative measures:

To prevent large-scale problems like this from occurring in the future, code should never be deployed to all servers prior to testing. Some things to consider for the future are: developing an enterprise-wide test protocol, setting up isolated docker containers for testing purposes, and implementing a two-person sign-off before a major deployment.
