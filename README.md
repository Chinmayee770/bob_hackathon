# BANK OF BARODA HACKATHON

# Walter White: Generative AI-Powered Dashboard for Enhanced Operations and Loan Approvals

**Team Cyber Wardens**  
**College: Vishwakarma Institute of Technology**  
**Team Members:**
- Pratham Gadkari
- Suraj Chavan
- Anuj Tadkase

---

## Problem Statement

The banking industry faces significant challenges in operational efficiency, particularly in repetitive administrative tasks and lengthy loan approval processes. Our project, Walter White, aims to address these challenges by creating a centralized dashboard that leverages Generative AI and Machine Learning. The main goals of the Walter White dashboard are to:

- **Retrieve and Analyze Customer Data:** Automatically fetch, store, and process customer data to support informed decision-making.
- **Perform Repetitive Calculations:** Automate financial calculations and metrics to reduce manual effort and minimize errors.
- **Categorize and Respond to Emails:** Use AI to classify incoming emails and generate appropriate responses, improving communication efficiency.
- **Streamline Loan Approvals:** Automate the loan approval process, reducing approval time from weeks to days.

---

## Methodology

### Overview
The Walter White dashboard integrates various Azure services and machine learning models to automate and streamline banking operations. Here’s a detailed breakdown of how each component functions:

### 1. Data Collection and Preprocessing
- **Input:** Business balance sheets (audited) in Excel format.
- **Azure Blob Storage:** Stores the uploaded Excel files.
- **Azure Functions:** Triggered when a new file is uploaded to Blob Storage.
  - **Action:** Read the Excel file, preprocess the data, and convert it to SQL database tables.
  - **Reference:** [Building an Azure Function to Process Excel Files](https://medium.com/@ynskrn54/building-an-azure-function-to-process-excel-files-from-blob-storage-and-store-datain-azure-sql-312947e21674)

### 2. Financial Ratio Calculation
- **Azure SQL Database:** Performs key financial ratio calculations (e.g., current ratio, debt-to-equity ratio) using SQL queries.
  - **Reference:** [Credit Analysis Ratios](https://corporatefinanceinstitute.com/resources/commercial-lending/credit-analysis-ratio/)

### 3. External Data Integration
- **Azure Logic Apps:** Automates fetching news articles related to businesses using a News API.
- **Azure Cognitive Services:** Analyzes news sentiment and searches for pending legal cases.
  - **Reference:** [Sentiment Analysis of News Headlines](https://medium.com/@ramitsharma1994.rs/sentiment-analysis-of-news-headlines-with-microsoft-azure-cognitive-services-be3dedf3ccec)

### 4. Auditing Agency Verification
- **Verification Process:** Ensures that all financial and external data meet required standards.
  - **Reference:** [Satyam Scam Overview](https://www.5paisa.com/blog/satyam-scam)

### 5. Lang-Chain for Database Retrieval and analytics
- **Azure Functions:** Uses Lang-Chain and Azure AI for efficient database retrieval and analytics based on predefined prompts.
  - **Reference:** [Chat with MySQL using Python and LangChain](https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/)
  - reference 2: analytics

### 6. Loan Approval Process
- **Verification:** Checks if financial ratios, external data, and audit verifications meet thresholds.
- **Azure Functions:** Implements logic for threshold checks and validation.
- **Approval:** Grants loan approval if all checks are satisfactory.
  - **Reference:**)

###6.5. - **(There will be a final validation from human side also to check if input documents is same as balnce sheet.csv- **

### 7. Customer (Non-Businesses) Credit Score Calculation
- **Azure Machine Learning:** Uses an improved ML model to calculate credit scores for non-business customers.
  - **Reference:** [Credit Score Anomaly Detection](https://github.com/ANUJT65/bob_hackathon/blob/main/backend/Credit_ScoreAnamolyDetection.ipynb)

### 8. Email Categorization and Response
- **Azure Cognitive Services:** Classifies incoming emails based on content and keywords and shows on dashboard
- **Azure Functions:** Generates and sends automated responses using Generative AI from centralized dashboard
  - **Reference:** [Python Gmail Auto Responder using ChatGPT](https://medium.com/@mehmetcan.oralalp/python-gmail-auto-responder-using-chatgpt-7f3a0fe4651c)

---
## IMPLEMENTATION

![Customer](https://github.com/ANUJT65/bob_hackathon/assets/123918593/3652dca0-5b93-4c42-9f94-38526886873b)

![WhatsApp Image 2024-06-22 at 2 22 43 AM](https://github.com/ANUJT65/bob_hackathon/assets/123918593/d53f7199-56ef-4fd0-b52e-c159ce729ad7)
![WhatsApp Image 2024-06-22 at 2 22 42 AM](https://github.com/ANUJT65/bob_hackathon/assets/123918593/91f32f14-1511-472a-9518-0f815c0b7035)
![WhatsApp Image 2024-06-22 at 2 22 42 AM (2)](https://github.com/ANUJT65/bob_hackathon/assets/123918593/0b0be6ab-66bb-4454-9c22-b2e57aa5310d)

---
## Uniqueness of Approach

### Comprehensive Automation
Walter White uniquely combines multiple functionalities into a single platform, including:
- **Customer Communication:** Streamlines interactions with customers through AI-driven email responses and automated workflows.
- **Internal Workflow Management:** Automates internal processes, reducing the workload on employees and increasing efficiency.
- **Unified Dashboard:** Provides a centralized interface for all banking operations, enhancing user experience and productivity.

### Integration of Generative AI
- **Textual Queries:** Utilizes Generative AI for answering textual queries, providing intelligent insights, and automating decision-making processes.
- **Data Analytics:** Applies AI for data classification, analysis, and generating actionable insights.

### Reduced Training Overhead
- **User-Friendly Interface:** Simplifies user interactions with the system, reducing the need for extensive employee training.
- **Humane Chatbot Experience:** Enhances the user experience with a conversational AI interface.

---

## Security Considerations

### Data Security
- **Advanced Encryption:** All sensitive data is encrypted both in transit and at rest using industry-standard encryption protocols.
- **Access Control:** Implements Azure Multi-Factor Authentication (MFA) and Role-Based Access Control (RBAC) to ensure that data access is restricted to authorized personnel only.
  - **References:**
    - [Azure Role-Based Access Control](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
    - [Azure Multi-Factor Authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks)

### Regular Security Updates
- **Automated Update Systems:** Utilizes automated systems for timely software updates and security patches to protect against emerging threats.
- **Testing Environment:** Deploys updates in a controlled testing environment to ensure they do not disrupt existing functionalities before full deployment.

### Performance Monitoring
- **Real-Time Monitoring:** Continuously monitors system performance and health to proactively identify and resolve issues.
- **Security Audits:** Conducts regular security audits and compliance checks to ensure the integrity and security of the platform.

---
## Tech Stack

### Frontend
- **React JS:** For building a dynamic and responsive user interface.

### Backend
- **Node JS:** For building scalable server-side applications.
- **Flask:** For developing RESTful APIs and handling backend logic.

### Machine Learning and AI
- **Azure Machine Learning:** For building and deploying machine learning models.
- **Azure Cognitive Services:** For natural language processing, sentiment analysis, and other AI-driven tasks.
- **Lang-Chain:** For efficient database retrieval and analytics.

### Data Storage and Processing
- **Azure Blob Storage:** For storing uploaded files and large datasets.
- **Azure SQL Database:** For storing and querying structured data.
- **Azure Data Factory:** For orchestrating data workflows and processing.

### Automation and Integration
- **Azure Functions:** For running serverless code triggered by events such as file uploads or HTTP requests.
- **Azure Logic Apps:** For automating workflows and integrating with external services.

### Security
- **Azure Multi-Factor Authentication (MFA):** For securing user access.
- **Role-Based Access Control (RBAC):** For managing permissions and access levels.
