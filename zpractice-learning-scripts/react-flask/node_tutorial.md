# NPM (Node Package Manager) Tutorial

## Introduction
NPM (Node Package Manager) is the default package manager for JavaScript runtime Node.js. It allows developers to install, share, and manage dependencies in JavaScript projects.

## Installation
Before using npm, you need to install Node.js, which includes npm by default.

### Install Node.js
- Download and install from [Node.js official website](https://nodejs.org/)
- Check installation:
  ```sh
  node -v  # Check Node.js version
  npm -v   # Check npm version
  ```

## Initializing a Project
To create a new project and generate a `package.json` file:
```sh
npm init
```
This will prompt a series of questions to configure your project. To create a default `package.json`, use:
```sh
npm init -y
```

## Installing Packages
### Installing a Single Package
```sh
npm install <package-name>
```
Example:
```sh
npm install express
```

### Installing a Package Globally
```sh
npm install -g <package-name>
```
Example:
```sh
npm install -g nodemon
```

### Installing a Specific Version
```sh
npm install <package-name>@<version>
```
Example:
```sh
npm install lodash@4.17.21
```

### Installing Development Dependencies
```sh
npm install <package-name> --save-dev
```
Example:
```sh
npm install eslint --save-dev
```

## Uninstalling Packages
### Remove a Package
```sh
npm uninstall <package-name>
```
Example:
```sh
npm uninstall express
```

### Remove a Global Package
```sh
npm uninstall -g <package-name>
```

## Updating Packages
### Update All Packages
```sh
npm update
```

### Update a Specific Package
```sh
npm update <package-name>
```

## Managing Dependencies
### List Installed Packages
```sh
npm list
```
For globally installed packages:
```sh
npm list -g --depth=0
```

### Checking for Outdated Packages
```sh
npm outdated
```

### Checking for Vulnerabilities
```sh
npm audit
```
To fix vulnerabilities:
```sh
npm audit fix
```

## Running Scripts
Define scripts in `package.json`:
```json
"scripts": {
  "start": "node app.js",
  "test": "jest"
}
```
Run a script:
```sh
npm run start
```

## Clearing Cache
If you encounter issues, clear npm cache:
```sh
npm cache clean --force
```

## Removing `node_modules` and Reinstalling Dependencies
```sh
rm -rf node_modules package-lock.json
npm install
```

## Conclusion
NPM is an essential tool for JavaScript development. Understanding how to install, update, and manage dependencies is crucial for efficient development. Explore the [npm documentation](https://docs.npmjs.com/) for more details.