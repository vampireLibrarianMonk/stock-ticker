Introduction

In the dynamic intersection of technology and finance, there's an increasing demand for tools that simplify investment tracking for end users. My project, a stock/commodity/item price tracking application is designed to meet this rudimentary requirement. Central to this project is the creation of an end-to-end, database-driven website using Django, with dependency management support of conda, the portability/isolation of the docker containerization strategy and the entire development lifecycle managed and automated through AWS CodePipeline.

Although simple in its conception, the need for a tracking application is just one foundational step in financial literacy serving as a potential foothold into taking a more proactive approach to portfolio monitoring and management. Having never programmed an end-to-end application before I want to flush out this subject and implement the application using Development Operations (DevOps) techniques I learned at my job and the applications I have not had a chance to use but have learned.

Project Overview

The primary goal of this stock market portfolio is to offer a comprehensive, widely available application capable of executing create, read, update and delete (CRUD) operations through a REST API, with a focus on persistent data storage. This application is tailored for users desiring an organized and efficient way to view their stock, commodity, or item portfolios.

TODO: 
	1. Upgrade app to 5.3
	2. Ensure error handling is initiated
	3. flush out user interface

Technology Stack and Development Approach

Python and Django are at the heart of this project. Their blend of simplicity and robustness is ideal for web application development. The project follows a beginner-friendly approach, guiding through the development of this app with Django. The emphasis on Django is significant as it's a high-level framework promoting rapid and clean development.

Key Application Aspects:

Django: Laying the foundation for web app development.

  * Building Database-Driven Websites: Vital for managing stock market data storage and retrieval.
  * Using APIs in Django: Integral for real-time financial data integration from third-party services.
  * Basic CSS with Bootstrap: Ensuring the application is both functional and aesthetically pleasing.
  * Integrating CRUD Operations
  * Django's ORM system inherently supports CRUD operations, which are essential for data management within applications. This will enable users to seamlessly add, view, update, or delete stocks in their portfolio, interacting effectively with the database.

CodePipeline Integration Aspects (Code Commit --> Code Build --> Code Deploy):

  * Automated Pipeline: Automates the build, test, and deployment phases, ensuring consistent quality and efficiency.
  * Continuous Integration/Continuous Deployment (CI/CD): Streamlines updates, with immediate testing and deployment of changes, reducing downtime and errors.
  * Scalability and Security: AWS infrastructure provides a scalable and secure environment for hosting the application.

To manage the dependencies of the application efficiently, Conda is integrated. Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. It easily creates, saves, loads, and switches between environments on your local computer. This feature is particularly beneficial for:

Conda for Dependency Management:

  * Managing Libraries and Dependencies: Ensuring that all required Python packages and libraries are consistent and compatible across all development and production environments.
  * Isolated Environments: Allowing different versions of packages to be maintained in separate environments, avoiding conflicts and aiding in smooth application functioning.
  * Simplifying Deployment: Streamlining the deployment process by managing the Python environment and dependencies.

TODO:
	1. create conda yml

Containerization using Docker

  * Consistent Environments: Docker containers provide consistent environments across development, testing, and production, eliminating the "it works on my machine" problem.
  * Isolation: Containers are isolated from each other, reducing conflicts between different parts of the application or with other applications.
  * Portability: Docker containers can be run on any system that supports Docker, simplifying deployment across different platforms and cloud providers.
  * Integration with AWS CodePipeline: Docker containers can be built, tested, and deployed using AWS CodePipeline, creating a seamless CI/CD pipeline.

TODO:
	1. create dockerfile

Conclusion

My stock market portfolio is more than a technical project; it's a bridge to more accessible financial monitoring tools. It stands as an exemplar for learning and applying Django's capabilities in CRUD operations, database management, and API integration. Combined with the power of AWS CodePipeline, this project not only assists in meeting academic criteria but also expanding my existing developer skills in end-to-end application development and providing a showcase for a foundational financial operations platform. The end result is a tool that's both comprehensive for tracking investments and a testament to modern software development practices.
