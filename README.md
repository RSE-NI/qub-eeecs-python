# QUB EEECS Python Course
## Agenda

| **Time** |  **Module**                                         | **Instructor** |
|----------|-----------------------------------------------------|----------------|
|          |  _Day one_                                          |                |
| 09.00    | _0. Environment set up clinic_                      | DC / RB        |
| 10.00    |  1. Unix shell 101                                  | RB             |
| 11.00    |  2. Command-line programs                           | RB             |
| 12.30    |  _Lunch_                                            |                |
| 14.00    |  3. Python fundamentals                             | RB             |
| 14.45    |  4. Structuring your code                           | DC             |
|          |                                                     |                |
|          |  _Day Two_                                          |                |
| 10.00    |  5. Loading and analyzing data from various sources | DC             |
| 11.00    |  6. Visualizing data                                | DC             |
| 12.30    |  _Lunch_
| 14.00    |  7. Errors and exceptions                           | DC             |
| 14.45    |  8. Testing your code                               | RB             |
|          |                                                     |                |
|          |  _Day Three_                                        |                |
| 10.00    |  9. Version Control with Git                        | RB             |
| 10.30    |  10. Creating a repository & tracking changes       | RB             |
| 11.30    |  11. Collaborating with others                      | DC             |
| 12.30    |  _Lunch_
| 14.00    |  12. Allowing others to run your code               | DC             |
| 14.30    |  13. Sustainable & maintainable code.               | DC             |
| 15.00    |  14. Getting a publication for your code            | DC             |


## Pre-requisites

To attend this course successfully, you must have the following installed by the end of the 'Environment set up clinic' on day one.  You are *strongly* advised to have this working on your own machine in advance, with all checks completed.  If you do not want to install directly to your machine, and you're comfortable with Docker or containers, you can go to the Installation with a Docker image section and follow the instructions.  If you run into issues, you can avail of help at the set-up clinic.

### Install Anaconda

Go to https://www.anaconda.com and download the Anaconda python distro.  This should automatically detect your operating system, but if not go to https://www.anaconda.com/products/distribution#Downloads and select the correct one.  Run the installer, pour yourself a coffee and put your feet up - this can take up to 20 mins or so. For Windows, MAKE SURE TO CHECK "ADD ANACONDA TO MY PATH ENVIRONMENT VARIABLE".

Once installed, run the application and it may ask you to update to 2.2.0, you can choose to go ahead and update (takes 2-3 mins) or not.  If you do, restart Anaconda. Verify that you can see the main Anaconda screen.  Click Jupyter Lab, and ensure it runs ok on your machine.

### Install Bash (and Git)

Please go to https://carpentries.github.io/workshop-template/#shell and follow the installation instructions carefully for your OS, selecting the options outlined. MacOS and Linux users will likely have these already.  However, you may not have Git installed.  Go to https://carpentries.github.io/workshop-template/#git and follow the verification or installation instructions.


### Installation with a Docker image

If you have installed directly to your machine, you don't have to worry about this section.  This is ONLY if you wish to run the necessary tools under a container environment and have Docker installed (https://docs.docker.com/get-docker/).

Fire up a terminal and enter `docker pull continuumio/anaconda3`  

Followed by:

`docker run -i -t -p 8888:8888 continuumio/anaconda3 /bin/bash -c "conda install jupyter -y --quiet && mkdir -p /opt/notebooks && jupyter lab  --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root"`

### Checking your installation

#### Windows: 
Open Git Bash and type `git --version` at the `$` prompt.  You should see something like `git version 2.36.1.windows.1`.  Then type `python -m this` and you should get some text output.
#### Linux
Open a terminal and type `git --version` at the `$` prompt.  You should see something like `git version 2.36.1.windows.1`.  Then type `python -m this` and you should get some text output.
#### Mac
Open a terminal and type `git --version` at the `$` prompt.  You should see something like `git version 2.36.1.windows.1`.  Then type `python -m this` and you should get some text output.


