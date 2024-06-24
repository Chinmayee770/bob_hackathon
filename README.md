# Bank Of Baroda Hackathon

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
  - **Reference for types of credit ratios:** [Credit Analysis Ratios](https://corporatefinanceinstitute.com/resources/commercial-lending/credit-analysis-ratio/)

### 3. External Data Integration
- **Azure Logic Apps:** Automates fetching news articles related to businesses using a News API.
- **Azure Cognitive Services:** Analyzes news sentiment and searches for pending legal cases.
  - **Reference for how sentiment analysis will be done:** [Sentiment Analysis of News Headlines](https://medium.com/@ramitsharma1994.rs/sentiment-analysis-of-news-headlines-with-microsoft-azure-cognitive-services-be3dedf3ccec)

### 4. Auditing Agency Verification
- **Verification Process:** Ensures that all financial and external data meet required standards.
  - **Reference for why its necessary??:** [Satyam Scam Overview](https://www.5paisa.com/blog/satyam-scam)

### 5. Lang-Chain for Database Retrieval and analytics
- **Azure Functions:** Uses Lang-Chain and Azure AI for efficient database retrieval and analytics based on predefined prompts.
  - **Reference for how its done:** [Chat with MySQL using Python and LangChain](https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/)
  - **reference 2 for how its going to be done:** [Chat Gen Ai and LangChain based analytics](https://github.com/ANUJT65/bob_hackathon/blob/main/backend/Using%20Pandas%20Dataframe%20Agent.ipynb/)

### 6. Loan Approval Process
- **Verification:** Checks if financial ratios, external data, and audit verifications meet thresholds.
- **Azure Functions:** Implements logic for threshold checks and validation.
- **Approval:** Grants loan approval if all checks are satisfactory.
  - **Reference:**)

###6.5. - **(There will be a final validation from human side also to check if input documents is same as balnce sheet.csv- **

### 7. Customer (Non-Businesses) Credit Score Calculation
- **Azure Machine Learning:** Uses an improved ML model to calculate credit scores for non-business customers.
  - **Reference of the prototype model:** [Credit Score Anomaly Detection](https://github.com/ANUJT65/bob_hackathon/blob/main/backend/Credit_ScoreAnamolyDetection.ipynb)

### 8. Email Categorization and Response
- **Azure Cognitive Services:** Classifies incoming emails based on content and keywords and shows on dashboard
- **Azure Functions:** Generates and sends automated responses using Generative AI from centralized dashboard
  - **Reference for the model:** [Python Gmail Auto Responder using ChatGPT](https://medium.com/@mehmetcan.oralalp/python-gmail-auto-responder-using-chatgpt-7f3a0fe4651c)
 
    ## Methodology

### 1. Data Input and Preprocessing
- **Excel Sheets:**
  - **Azure Blob Storage:** Store the uploaded Excel files.
  - **Azure Functions:** Triggered when a new file is uploaded to Blob Storage.
    - **Action:** Read the Excel file, preprocess the data, and convert it to SQL database tables.
    - **Reference:** [Building an Azure Function to Process Excel Files](https://medium.com/@ynskrn54/building-an-azure-function-to-process-excel-files-from-blob-storage-and-store-data-in-azure-sql-312947e21674)

- **OCR using Azure Form Recognizer:**
  - **Azure Form Recognizer:** Extracts structured data from scanned documents and forms.
  - **Azure Functions:** Processes the extracted data and stores it in the database.
    - **Reference:** [Introduction to Azure Form Recognizer](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/)

- **Direct Keyboard Inputs:**
  - **Web Interface:** Provides forms for users to input data manually.
  - **Azure Functions:** Handles form submissions and updates the database accordingly.

### 2. Financial Ratio Calculation
- **Azure SQL Database:** Performs key financial ratio calculations (e.g., current ratio, debt-to-equity ratio) using SQL queries.
- **Customer Credit Score Calculation:**
  - **Azure Machine Learning:** Uses an improved ML model to calculate credit scores for non-business customers based on their financial data.
  - **Integration:** Incorporates credit score calculation with financial ratios for a comprehensive assessment.
  - **Reference:** [Credit Score Anomaly Detection](https://github.com/ANUJT65/bob_hackathon/blob/main/backend/Credit_ScoreAnamolyDetection.ipynb)
  - **Reference:** [Credit Analysis Ratios](https://corporatefinanceinstitute.com/resources/commercial-lending/credit-analysis-ratio/)

### 3. External Data Integration
- **Azure Logic Apps:** Automates fetching news articles related to businesses using a News API.
- **Azure Cognitive Services:** Analyzes news sentiment and searches for pending legal cases.
- **Integration:** Uses external data to enhance credit score and financial assessment.
  - **Reference:** [Sentiment Analysis of News Headlines](https://medium.com/@ramitsharma1994.rs/sentiment-analysis-of-news-headlines-with-microsoft-azure-cognitive-services-be3dedf3ccec)

### 4. Auditing Agency Verification
- **Verification Process:** Ensures that the audited balance sheet is reliable and verified by a reputable auditing agency.
- **Integration:** Combines verification results with financial ratios and external data for comprehensive loan assessment.
  - **Reference:** [Satyam Scam Overview](https://www.5paisa.com/blog/satyam-scam)

### 5. Lang-Chain for Database Retrieval
- **Azure Functions:** Uses Lang-Chain and Azure AI for efficient database retrieval and analytics based on predefined prompts.
- **Integration:** Supports real-time data retrieval and analysis for loan processing and customer support.
  - **Reference:** [Chat with MySQL using Python and LangChain](https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/)

### 6. Loan Approval Process
- **Verification:** Checks if financial ratios, external data, and audit verifications meet thresholds.
- **Azure Functions:** Implements logic for threshold checks and validation.
- **Approval:** Grants loan approval if all checks are satisfactory.
- **Customer (Non-Businesses) Credit Score Calculation:** Uses Azure ML model to incorporate credit scores in the loan approval process.
  - **Reference:** [Credit Score Anomaly Detection](https://github.com/ANUJT65/bob_hackathon/blob/main/backend/Credit_ScoreAnamolyDetection.ipynb)

### 7. Email Categorization and Response
- **Azure Cognitive Services:** Classifies incoming emails based on content and keywords.
- **Azure Functions:** Generates and sends automated responses using Generative AI.
  - **Integration:** Automated responses and communications during the loan approval process and other customer interactions.
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

Security is a critical component of the Walter White Dashboard. We are leveraging several security measures and best practices to ensure the confidentiality, integrity, and availability of our system. Below are the key security considerations implemented in our project:

### 1) Authentication and Authorization

- **Microsoft Authentication Library (MSAL)**: We use MSAL for secure user authentication and authorization. This allows users to authenticate using Azure Active Directory (Azure AD), ensuring that only authorized personnel can access sensitive information.
  - [Authentication with Azure AD and React](https://adrianhynes.medium.com/authentication-with-azure-ad-and-react-ced9a829e083)
  - [Secure Your React.js Web Application with Azure AD Authentication Using MSAL Library](https://medium.com/@isuruariyarathna2k00/secure-your-react-js-web-application-with-azure-ad-authentication-using-masl-library-7f578c65f209)

### 2) Multi-Factor Authentication (MFA)

- **Multi-Factor Authentication (MFA)**: We implement MFA to add an extra layer of security. Options include:
  - **Email OTP**: Sending a one-time password to the user's registered email address.
  - **Microsoft Authenticator App**: Using the app for code generation, which must be entered along with the password.
  - [Azure Multi-Factor Authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks)

### 3) Role-Based Access Control (RBAC)

- **Role-Based Access Control (RBAC)**: Different roles have different levels of access:
  - **Bank Manager**: Full access to all emails, chat records, and loan applications.
  - **Employees**: Limited access to view emails assigned to them and approve/decline loan applications without editing the database.
  - **Customers**: Access only to their own emails and loan applications.
  -  [Azure Role-Based Access Control](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

### 4) Data Security

- **Azure SQL Database**: Storing data securely using Azure SQL Database with encryption at rest and in transit.
- **Azure Blob Storage**: Securely storing documents and forms in Azure Blob Storage.

### 5) Secure Data Transfer

- **HTTPS**: All data exchanges between the client and server are encrypted using HTTPS to prevent eavesdropping and man-in-the-middle attacks.

### 6) Auditing and Monitoring

- **Audit Logs**: Implementing detailed audit logs to monitor access and changes to sensitive information. This helps in tracking and identifying any unauthorized access or modifications.
- **Azure Security Center**: Using Azure Security Center to continuously monitor and improve the security posture of our resources.

### 7) Verification of Auditing Agencies

- **Auditing Agency Verification**: Ensuring that balance sheets and financial documents are verified by reputable auditing agencies. This prevents fraud and enhances the trustworthiness of submitted documents.

By implementing these comprehensive security measures, we ensure that our system is robust against various security threats and complies with industry standards for data protection and privacy.



---
## Tech Stack

### Frontend
- **React JS:** For building a dynamic and responsive user interface.

### Backend
- **Node JS:** For building scalable server-side applications.
- **Flask:** For developing RESTful APIs and handling backend logic.

### Machine Learning and AI
- **Azure Machine Learning:** For building and deploying machine learning models.
- **Azure Cognitive Services:** For natural language processing, sentiment analysis,email classification,external data integration and other AI-driven tasks.
- **Lang-Chain:** For efficient database retrieval and analytics.
- **Azure Generative AI:** for doing analytics ,for responding to emails etc.

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
