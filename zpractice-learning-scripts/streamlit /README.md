# Streamlit

## What is Streamlit?

Streamlit is an open-source Python library that allows you to create and share beautiful, custom web apps for machine learning and data science. Its simplicity and ease of use make it a popular choice among developers. With just a few lines of Python code, you can create interactive dashboards and applications without needing to worry about web development frameworks.

Streamlit works by converting Python scripts into web applications. When you run a Streamlit script, it launches a local web server and renders the application in your browser. It automatically detects changes in the script and updates the UI in real time, making the development process smooth and efficient.

## Understanding How Streamlit Works

Streamlit automatically watches for changes in your Python script and refreshes the UI when you save the file. It follows a reactive programming model, meaning that whenever an input widget is modified, the script is re-executed from top to bottom to reflect the updated state.

Some key aspects of Streamlit’s working mechanism:
- **Stateless Execution**: Every user interaction triggers a full rerun of the script.
- **Caching with `@st.cache_data`**: You can cache expensive computations to improve performance.
- **Session State (`st.session_state`)**: Enables stateful behavior across interactions.

## Building a Simple App

To build a basic Streamlit app, follow these steps:

#### Title and Text:
- `st.title("My First Streamlit App")` sets the title for your app.
- `st.write()` is used to display text and variable values.
- `st.markdown()` allows rendering formatted text using Markdown.

#### Widgets:
- `st.slider("Pick a number", 0, 100, 50)` creates an interactive slider widget for user input.
- `st.button("Click Me")` creates a button that can trigger an action.
- `st.text_input("Enter your name")` collects user input as text.
- `st.checkbox("Accept terms")` creates a simple checkbox for boolean input.

#### Charts and Data:
- Streamlit supports displaying various types of data visualizations. You can use built-in functions like:
  - `st.line_chart(data)`: Displays a line chart from a DataFrame.
  - `st.bar_chart(data)`: Renders a bar chart.
  - `st.map(data)`: Displays geographical data on a map.

#### st.set_page_config 
Streamlit is used to configure the initial appearance and behavior of your web app’s page. Here’s what it does:
- `page_title`: The title of the web page.
- `page_icon`: The favicon for the web page.
- `layout`: The layout of the app (wide or centered).
- `initial_sidebar_state`: The state of the sidebar (expanded or collapsed).
- `menu_items`: The items to display in the hamburger menu.
- `menu`: The items to display in the hamburger menu.
- `theme`: The theme of the app (light or dark).
- `primaryColor`: The primary color of the app.
- `backgroundColor`: The background color of the app.

#### st.session_state
Streamlit’s `st.session_state` allows you to store and access user-specific data across different interactions. It is useful for maintaining stateful behavior in your app.


## Running the App

To run your Streamlit app, navigate to the directory where your `app.py` is located and run the following command in your terminal:

```sh
streamlit run app.py
```

A new browser window will open displaying your app. If it doesn't open automatically, check the terminal for the local URL (usually `http://localhost:8501`) and open it manually.


