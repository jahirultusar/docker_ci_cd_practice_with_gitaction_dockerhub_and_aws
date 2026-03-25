[![CI/CD Pipeline](https://github.com/jahirultusar/docker_ci_cd_practice_with_gitaction_dockerhub_and_aws/actions/workflows/cicd.yml/badge.svg)](https://github.com/jahirultusar/docker_ci_cd_practice_with_gitaction_dockerhub_and_aws/actions/workflows/cicd.yml)

## This is a CI/CD practice codebase with Docker, Dockerhub and AWS EC2

The Tech Stack:

    Backend: Python 3.11 / Flask 
    Frontend: Bootstrap 3.4.1 
    Container: Docker (Alpine Linux for minimal footprint)
    Code Registry: Dockerhub & Git 
    CI/CD: GitHub Actions (Automated testing and deployment)
    Infrastructure: AWS EC2 

Dashboard Features:

    Live System Logs: Captures incoming HTTP requests and streams them to the UI without page refreshes.
    Health Diagnostics: Monitors system stability, including Uptime, Process ID, and Network Latency.
    Network Telemetry: Displays the Container ID and Internal IP, mapping the private Docker network to the public user.
    Self-Healing: A built-in Docker HEALTHCHECK ensures the container automatically reports as (unhealthy) if the Flask process hangs.


How to Run Locally:

    Clone the Repo: 
        git clone <this-repo-url>
    
    Build the Image:
        docker build -t my-machine .
    
    Launch the Container:
        docker run -p 80:5001 my-machine
    
    Access the Dashboard: Open http://localhost:80

Deployment Traceability:

```
Every deployment is "stamped" with its unique Git Hash and Build Timestamp in the footer, ensuring 100% traceability between the code in GitHub and the running version on AWS.
```

Maker: JI |
Status: PROD-READY 