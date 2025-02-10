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
### Functional Requirements

The company aims to develop a **language learning platform** that provides an **interactive and immersive experience** for students.  

There is a strong emphasis on **data privacy**, as the organization is concerned about storing **user data securely** while reducing reliance on **third-party managed AI services**, which may become costly in the long run.  

To achieve this, they plan to **invest in their own AI infrastructure**, specifically **an AI PC** with a budget range of **$10,000 to $15,000**.  

Currently, the platform serves **300 active students**, all of whom are located within the city of **Nagasaki**.  

### Assumptions  

- We assume that the AI-powered **sentence constructor** and **study activities** will significantly improve student engagement and retention.  
- The system will rely on a **local database** (Lang Core 2000 words) while integrating **retrieval-augmented generation (RAG)** for sentence-building tasks.  
- The company is **prioritizing self-hosted AI solutions** over cloud-based alternatives to **maintain control over operational costs and privacy concerns**.  
- The payment system will be **seamlessly integrated** into the Lang Portal, ensuring **easy access** for students while supporting **teacher involvement** in learning sessions.  

### Considerations  

- The AI model should be **self-hosted** to ensure **data privacy** and **cost control**, reducing dependency on third-party cloud services.  

- We need to ensure that the **RAG system** used for **sentence construction** can **retrieve relevant language data efficiently** while maintaining accuracy.  

- The platform must be **scalable** to accommodate more than **300 students** in the future while ensuring smooth performance for existing users.  

- The **payment gateway** should support **local and international transactions** while ensuring compliance with **security standards** like **PCI-DSS**.  

- We need a **monitoring system** to track **AI performance**, detect biases, and ensure that **generated content aligns** with educational objectives.  

## Estructure

### Backend (Flask API)

- **Python** with **Flask** as the web framework
- **SQLite3** as the database
- **Flask-CORS** for handling Cross-Origin Resource Sharing
- **Invoke** for task running/automation
- **Pytest** for testing

### Frontend (React App)

Based on the frontend prompt requirements:

- **React.js** as the frontend library
- **TypeScript** as the programming language
- **Tailwind CSS** for styling
- **Vite.js** as the development server/bundler
- **ShadCN** for UI components
