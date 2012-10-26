# \#CAA IRC Bot Quote Viewer

## Installation Instructions
1.  Checkout the repo to a non-public directory
1.  Create a .fcgi script (or other script) so that Apache (or whatever webserver)
1.  Create a .htaccess file (or equivalent host configuration) so that all requests for "/quotes/.*" get sent to that .fcgi script
1.  In the checked out directory, copy settings.py-default to settings.py, and then edit:
    *  the ENGINE under the 'default' database
    *  the NAME under the 'default' database
    *  Add the absolute path of the template directory checked out along with the repo to TEMPLATE_DIRS
      * Note that this should probably end with "caa_quotes/caaquotes/templates"