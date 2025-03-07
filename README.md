# GenAI Bootcamp - Language Learning Platform

--------------------------------------------------------------------------------
## Bootcamp Description  

In this bootcamp, I will develop a **self-hosted AI-powered language learning platform**

The bootcamp covers:  

- **AI-driven sentence construction and study tools** to enhance language learning.  
- **Retrieval-Augmented Generation (RAG)** techniques for improved contextual accuracy.  
- **Full-stack development** using **Flask (backend) and React.js (frontend)**.  
- **Local AI model hosting** to reduce dependency on third-party services.  


## Application Overview
#### - Functional Requirements

The company aims to develop a **language learning platform** that provides an **interactive and immersive experience** for students.  

There is a strong emphasis on **data privacy**, as the organization is concerned about storing **user data securely** while reducing reliance on **third-party managed AI services**, which may become costly in the long run.  

To achieve this, they plan to **invest in their own AI infrastructure**, specifically **an AI PC** with a budget range of **$10,000 to $15,000**.  

Currently, the platform serves **300 active students**, all of whom are located within the city of **Nagasaki**.  

#### - Assumptions  

- We assume that the AI-powered **sentence constructor** and **study activities** will significantly improve student engagement and retention.  
- The system will rely on a **local database** (Lang Core 2000 words) while integrating **retrieval-augmented generation (RAG)** for sentence-building tasks.  
- The company is **prioritizing self-hosted AI solutions** over cloud-based alternatives to **maintain control over operational costs and privacy concerns**.  
- The payment system will be **seamlessly integrated** into the Lang Portal, ensuring **easy access** for students while supporting **teacher involvement** in learning sessions.  

#### - Considerations  

- The AI model should be **self-hosted** to ensure **data privacy** and **cost control**, reducing dependency on third-party cloud services.  

- We need to ensure that the **RAG system** used for **sentence construction** can **retrieve relevant language data efficiently** while maintaining accuracy.  

- The platform must be **scalable** to accommodate more than **300 students** in the future while ensuring smooth performance for existing users.  

- The **payment gateway** should support **local and international transactions** while ensuring compliance with **security standards** like **PCI-DSS**.  

- We need a **monitoring system** to track **AI performance**, detect biases, and ensure that **generated content aligns** with educational objectives.  

## Estructure

#### - Backend (Flask API)

- **Python** with **Flask** as the web framework
- **SQLite3** as the database
- **Flask-CORS** for handling Cross-Origin Resource Sharing
- **Invoke** for task running/automation
- **Pytest** for testing
- **ChromaDB** for storing and managing data for knowledge base

#### - Frontend (React App)

Based on the frontend prompt requirements:

- **React.js** as the frontend library
- **TypeScript** as the programming language
- **Tailwind CSS** for styling
- **Vite.js** as the development server/bundler
- **ShadCN** for UI components



----- 
## Journal

#### - Week 0: Project Kickoff

#### - Week 1: Backend Development

 Backend Project Setup

 1. Set up the project structure:

- Create a new directory for the backend project.
- Initialize a Python virtual environment.
- Install necessary dependencies (Flask, SQLite, and Mage).

 2. Define the database schema:

- Create an SQLite database named `words.db`.
- Define tables for words, word groups, study sessions, study activities, and word review items.

 3. Implement the API endpoints:

- Create endpoints for fetching and managing words, groups, study sessions, and study activities.
- Implement endpoints for dashboard statistics and reset operations.

 4. Set up task runner (Mage):

- Define tasks for initializing the database, running migrations, and seeding data.

 5. Test the API:

- Write tests to ensure all endpoints work as expected.
- Verify the database operations and API responses.




## AI coding tools

- Replit – Build apps and sites with AI https://replit.com
    Your own automated app developer · Start with a prompt. Prompt Replit Agent by describing the app or site you want to create.
- Vercel - https://vercel.com/
    Develop. Preview. Ship. For the best frontend teams – Vercel is the optimal workflow for frontend teams. All-in-one: Static and Jamstack deployment, Serverless Functions, and Global CDN.

## Other tools
-  Firecraker - https://firecracker-microvm.github.io/
Firecracker is an open-source virtualization technology that is purpose-built for creating and managing secure, multi-tenant container and function-based services that provide serverless operational models. Firecracker runs workloads in lightweight virtual machines, called microVMs, which combine the security and isolation properties provided by hardware virtualization technology with the speed and flexibility of containers.

-  CodeSandbox - https://codesandbox.io/
- 



