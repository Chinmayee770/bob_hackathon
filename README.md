# Bank Of Baroda Hackathon

# Walter White: Generative AI-Powered Centralized Dashboard for Enhanced Operations and Loan Approvals

**Team Cyber Wardens**  
**College: Vishwakarma Institute of Technology**  
**Team Members:**
- Pratham Gadkari
- Suraj Chavan
- Anuj Tadkase

---

## Problem Statement

The banking industry faces significant challenges in operational efficiency, particularly in repetitive administrative tasks and lengthy loan approval processes. Our project, Walter White, aims to address these challenges by creating a centralized dashboard that leverages Generative AI and Machine Learning.
 The main goals of the Walter White dashboard are to:
 
- **Streamline Loan Approvals:** Automate the loan approval process, reducing approval time from weeks to days(reducing the approval time for business loan approvals which take weeks, and also reducing the personal loan approvals which take upto some days).
- **Retrieve and Analyze Customer Data:** Automatically fetch, store, and process customer data to support informed decision-making.
- **Perform Repetitive Calculations:** Automate financial calculations and metrics to reduce manual effort and minimize errors.
- **Categorize and Respond to Emails:** Use AI to classify incoming emails and generate appropriate responses, improving communication efficiency.
  
---

## Prerequisites for understanding the project/Various considerations in project

### 1.Loan Approvals
## Business Loans
The parameters for giving business loans are very different from personal loans. The parameters considered include:
- Income tax returns
- Audited balance sheets

- [Audited Sheet example pdf](https://www.moneycontrol.com/financials/tatamotors/balance-sheetVI/TM03)
- [Audited Sheet inputs/parameters considered](https://drive.google.com/file/d/1voKSi_i6FulvfVyE1tcm8e6QSYBsdD8b/view?usp=sharing)

### Personal Loans
The parameters considered for personal loans are detailed in the following PDF:
- [Personal loan CIBIL score form for input](https://drive.google.com/file/d/1y1H42ZYHDpVyRy0YMS66Z_2i_ig3XX-0/view)

### 2. Email Classification and Categorization(Enhancing customer connect):
Scalable Machine learning models categorizes and classify emails sent to respective departments so that customers are prioritized and their queries are always resolved.
-[Categories Considered]()

### 3.Analytics and repititive calculations 
Using Generative AI and varius mathematical methods we are ensuring that analytics and calculations are automated and done with utmost ease.

## Methodology

### Overview
The Walter White dashboard integrates various Azure services and machine learning models to automate and streamline banking operations. Here’s a detailed breakdown of how each component functions:

![image](https://github.com/ANUJT65/bob_hackathon/assets/123918593/5ef69718-31ef-4825-b49b-fee883dc110d)

## Detailed Workflow


## For removing any confusion before we start :
- 1) Inputs can be through ocr , csvs and pdfs and even keyboard inputs for making it easy for customers to access the dashboard (Customer is king as they always say )
 - 2) Azure Blob storage is for storing documents.
- 3) Azure sql database is for storing structured information from documents and inputs.
### 4)
- **Please be free to zoom in to image and follow the numbers in diagram, their descriptions are given below accordingly**
- **Please be free to zoom in to image and follow the numbers in diagram, their descriptions are given below accordingly**
- **Please be free to zoom in to image and follow the numbers in diagram, their descriptions are given below accordingly**

 ![bobdiagram-Page-1 drawio (2)](https://github.com/ANUJT65/bob_hackathon/assets/123918593/a537a68d-79f3-42a0-ad0a-7b90a06df387)


### 1. Data Input and Preprocessing
 

**A)OCR using Azure Form Recognizer:**
- **Azure Form Recognizer:** Extracts structured data from scanned documents(Audited balance sheet pdfs,tax returns pdfs, cibil score pdfs) and forms.
- **Azure Functions:** Processes the extracted data and stores it in the database (blob storage)
  - **Reference: On how it will be implemented:** [Introduction to Azure Form Recognizer](https://medium.com/microsoftazure/extracting-form-data-to-json-excel-pandas-with-azure-form-recognizer-160488a2d11e)
 
**B)Excel Sheets:**
-  Business balance sheets (audited)  in Excel format will be stored on **Azure Blob Storage:**.
- **Azure Functions:**  is triggered when a new file is uploaded to Blob Storage.
  - **Action: taken:** Read the Excel file, preprocess the data, and convert it to SQL database tables.
  - **Reference:** [Building an Azure Function to Process Excel Files](https://medium.com/@ynskrn54/building-an-azure-function-to-process-excel-files-from-blob-storage-and-store-data-in-azure-sql-312947e21674)
    
**C)Direct Keyboard Inputs:**
- **Web Interface:** Provides forms for users to input data manually.
- **Azure Functions:** Handles form submissions and updates the database accordingly.
- all forms have been provided in prerequisites
  
### 2. Financial Ratio Calculation
- **Azure SQL Database:** Performs key financial ratio calculations (e.g., current ratio, debt-to-equity ratio) using SQL queries.(Gen ai for calculations is not reliable )
  - **Reference: on which ratios will be calculated and considered** [Credit Analysis Ratios](https://corporatefinanceinstitute.com/resources/commercial-lending/credit-analysis-ratio/)

### 3. External Data Integration
- **Azure Logic Apps:** Automates fetching of news articles related to businesses using a News API.
- **Azure Cognitive Services:** Ro Analyze news sentiment and searches for pending legal cases on companies.
  - **Reference: on how sentiment analysis is done** [Sentiment Analysis of News Headlines](https://medium.com/@ramitsharma1994.rs/sentiment-analysis-of-news-headlines-with-microsoft-azure-cognitive-services-be3dedf3ccec)

### 4. Auditing Agency Verification: (Check the reliability of the agency who audited the data)
- **Verification Process:** Ensures that all financial and external data meet required standards and also if the auditing agencies are proper or not who audited all this financial data.
- **Reference for why its necessary??:** [Satyam Scam Overview](https://www.5paisa.com/blog/satyam-scam)

### 5. Lang-Chain and Azure Gen AI for Database Retrieval and analytics
- **Azure Functions:** Uses Lang-Chain and Azure AI for efficient database retrieval and analytics based on predefined prompts.
- **Reference for how its done:[medium]** [Chat with MySQL using Python and LangChain](https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/)
- **reference 2 for how its going to be done:[git link]** [Chat Gen Ai and LangChain based analytics](https://github.com/ANUJT65/bob_hackathon/blob/main/backend/Using%20Pandas%20Dataframe%20Agent.ipynb/)
  
### 6. Loan Approval Process
- **Verification:** Checks if financial ratios, external data, and audit verifications meet thresholds.
- **Azure Functions:** Logic is implemented for threshold checks and validation.
- **Approval:** Final loan approval if all checks are satisfactory (input pdfs to input data is verified and final loan is approved).

### 7. Customer (Non-Businesses) Credit Score Calculation
- **Azure Machine Learning:** Will use an improved ML model to calculate credit scores for non-business customers.
  - **Integration with Step 6:** Uses customer data processed in steps 1-3 to calculate the credit score and validate during the loan approval process.
  - **Reference model[git link]** [Credit Score Anomaly Detection](https://github.com/ANUJT65/bob_hackathon/blob/main/backend/Credit_ScoreAnamolyDetection.ipynb)

### 8. Email Classification and Response
- **Azure Cognitive Services:** Classifies incoming emails based on content and keywords.
- **Azure Functions:** Generates and sends automated responses using Generative AI.
  - **Integration with Step 1:** As part of the data preprocessing, incoming emails are processed and categorized.
  - **Integration with Step 6:** Automated responses and communications during the loan approval process and other customer interactions.
  - **Reference:[git link]** [Python Gmail Auto Responder using ChatGPT](https://medium.com/@mehmetcan.oralalp/python-gmail-auto-responder-using-chatgpt-7f3a0fe4651c)

## Centralized Dashboard
- **Overview:** A centralized dashboard for monitoring and managing the entire process, providing a unified interface for data access and control.
- All the processed information, including department-wise email classification, financial ratios, company reputation, agency/audit check, business loan status, and personal loan status, is integrated into a centralized dashboard.
- This dashboard provides a comprehensive view for decision-makers to approve loans, respond to emails, and perform other critical operations efficiently.
  
-**Question/Query on Data:**
Users (bankers) can query or pose questions about data through the centralized dashboard, making the decision-making process more interactive and data-driven.

-**Data Chat Gen AI (Data Analytics):**
Data analytics is facilitated through AI using langchain and pandas agents to provide insights and trends through a humanised chat bot method.

#############
---
## IMPLEMENTATION

![Wireframe - 1](https://github.com/ANUJT65/bob_hackathon/assets/123918593/cd488880-7d46-4d61-b76a-0967e15898a4)

## Customer side:
## Desc of below image:
- As you can see in image, customers just have to attach their financial documents and azure ocr will do the work for them of filling the forms aswell as form recognition .
- This really improves engagement of users and makes the financial process less stressful.

![Wireframe - 6](https://github.com/ANUJT65/bob_hackathon/assets/123918593/c4381e5d-7989-43ea-83af-2659ec15d6cf)

## Desc of below image:
- This is the centralized dashboard for customer side where they can track their applications and whether they are approved or not.
-  Here you could see attachments necessary for businesses / customers which are all stored in bank database with automated calculations(specially balance sheets) 
    ensuring that customers dont have to deal with these.
![Wireframe - 5](https://github.com/ANUJT65/bob_hackathon/assets/123918593/e5dfce72-5e7a-4970-8332-23e37c652210)



## Banker Side:
## Desc:
- We can see how applications are categorised using ml model and  even a loan approval score is calculated so that they could be approved or declined.
- Even mails could be sent as shown below to customers through the dashboard itself to user on the basis of risk,
  like much more interest rate for risky users or rejection mails etc
  
![Wireframe - 2](https://github.com/ANUJT65/bob_hackathon/assets/123918593/bd72c41d-ef22-4a80-a86a-936aee510497)

## Desc:
- Here we could see categorization of incoming emails, which could be handled by respective departments and queries could be solved immediately boosting customer confidence.
![Wireframe - 3](https://github.com/ANUJT65/bob_hackathon/assets/123918593/128c5c3c-966d-449d-859f-1ea5e7d6ba1b)

#### Desc:
- This is one of our more innovative way of using generative ai where you could query the  database in natural language and get access to **read only** information
- Here you could also do analytics of the attached document or retrieved documents using pandas agent and azure gen ai whose basic implementation is provided in 
  this repo.
![Wireframe - 4](https://github.com/ANUJT65/bob_hackathon/assets/123918593/df72e034-e677-4f6d-862c-0b1d517d690f)

- 
### Easy Login:
## Desc:
- We tried to make the login process for customers as easy as possible through otp but didnt compromise on security, which you will see as follows:
![Wireframe - 8](https://github.com/ANUJT65/bob_hackathon/assets/123918593/c1e4bbd8-6c22-4929-a2d2-4712aac779f2)
![Wireframe - 9](https://github.com/ANUJT65/bob_hackathon/assets/123918593/38f0b253-e3a3-458e-b6fd-79aaf58aa874)


---
## Tech Stack

![Tech_Stack](https://github.com/ANUJT65/bob_hackathon/assets/123918593/2bb6736b-6088-408f-b53b-15dacd03fe3c)

### Frontend
- **React JS:** For building a dynamic and responsive user interface.

### Backend
- **Flask:** For developing RESTful APIs and handling backend logic and also for integrating azure tools aswell as machine learning and gen ai

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


