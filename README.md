# QUB EEECS Python Course

## Agenda

| **Time** | **Module**                                         | **Instructor** |
|----------|----------------------------------------------------|----------------|
|          | _Day one_                                          |                |
|          | 1. Environment set up clinic                       | DC / AB        |
|          | 2. Unix shell 101                                  | AB             |
|          | 3. Command-line programs                           | AB             |
|          | 4. Python fundamentals                             | AB             |
|          | 5. Structuring your code                           | DC             |
|          |                                                    |                |
|          | _Day Two_                                          |                |
|          | 6. Loading and analyzing data from various sources | DC             |
|          | 7. Visualizing data                                | DC             |
|          | 8. Errors and exceptions                           | DC             |
|          | 9. Testing your code                               | AB             |
|          |                                                    |                |
|          | _Day Three_                                        |                |
|          | 10. Version Control with Git                       | AB             |
|          | 11. Creating a repository & tracking changes       | AB             |
|          | 12. Collaborating with others                      | DC             |
|          | 13. Allowing others to run your code               | DC             |
|          | 14. Sustainable & maintainable code.               | DC             |
|          | 15. Getting a publication for your code            | DC             |


## Pre-requisites

To attend this course successfully, you must have the following installed by the end of the 'Environment set up clinic' on day one.  You are *strongly* advised to have this working on your own machine in advance, with all checks completed.  If you run into issues, you can avail of help at the set-up clinic.

-Install with a Docker image

`docker pull continuumio/anaconda3`
`docker run -i -t -p 8888:8888 continuumio/anaconda3 /bin/bash -c "\
    conda install jupyter -y --quiet && \
    mkdir -p /opt/notebooks && \
    jupyter lab --ip='*' --port=8888 \
    --no-browser --allow-root"
`

