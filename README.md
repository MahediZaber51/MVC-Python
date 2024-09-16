# Flask MVC Structure with Discord Integration

Welcome to the **Flask MVC Structure with Discord Integration**! This project is primarily a **Flask-based web application** following the MVC (Model-View-Controller) structure, with the added feature of integrating a **Discord bot** using **Disnake**. This setup allows you to build a web app while also having a Discord bot running in parallel, enabling additional functionality. The structure is flexible, allowing you to expand it for more parallel tasks, or easily adjust it to run a single task as needed.



## Project Structure

```bash
.
├── app
│   ├── Actions             # Utility functions (pagination, embeds, webhook handling, etc.)
│   ├── Commands            # Discord command handling
│   │   ├── Context         # Traditional Discord commands
│   │   └── Slash           # Slash commands for Discord
│   ├── Controllers         # Controller logic for Flask and Discord
│   │   ├── Flask           # Controllers specific to Flask web app
│   │   └── Discord         # Controllers for Discord bot
│   ├── Models              # Data models for the application
│   └── Views               # Dynamic Flask views/templates structures
├── config
│   └── boot.py             # Main entry point to boot up the program (Flask + Discord)
├── database
│   └── db.py               # Database interactions (abstraction layer)
├── resources                # Static and template files for Flask
│   ├── css                 # CSS files
│   ├── js                  # JavaScript files
│   └── views               # HTML templates
├── routes
│   ├── api.py              # Routes for API endpoints
│   └── web.py              # Routes for web pages
├── storage                  # User file storage (uploads, etc.)
├── vendor                   # Placeholder for third-party integrations (collaborations welcome)
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker containerization file
└── .env                     # Environment configuration variables
```

## Features Implemented

### Flask
- **MVC Structure**: Organized codebase that follows the MVC pattern for better separation of concerns:
  - **Models** handle data.
  - **Views** are rendered by Flask, found in `resources/views`.
  - **Controllers** handle business logic for web and API routes.
- **Routing**: 
  - API routes are defined in `routes/api.py`.
  - Web routes are in `routes/web.py`.
- **Database Abstraction**: Easy-to-extend database layer (`database/db.py`) for managing models.
- **Templates & Static Files**: Resources such as HTML, CSS, and JavaScript are stored in `resources/`.

### Discord Bot (Using Discord.py)
- **Commands**: 
  - Traditional text-based Discord commands in `app/Commands/Context`.
  - Slash commands in `app/Commands/Slash`.
- **Parallel Execution**: The Discord bot runs alongside the Flask application for seamless interaction between web and Discord functionalities.
- **Utility Actions**: Functions like pagination, embeds, and webhook handling in `app/Actions`.

### Docker
- **Containerization**: Provided `Dockerfile` allows you to run the entire application in a Docker container, simplifying the setup process.

## What's Next?

### To-Do
- [ ] **Vendor Integrations**: Open for contributions to implement third-party integrations or plugins within the `vendor/` directory.
- [ ] **Authentication**: Integrate authentication (OAuth or token-based) for the web app and APIs.
- [ ] **File Management**: Add advanced handling for user uploads within the `storage/` folder.
- [ ] **Error Handling & Logging**: Enhance error handling across both Flask and Discord components, with proper logging.

## Collaboration

Contributions are welcome! If you'd like to collaborate, feel free to fork this repository and submit a pull request. Potential areas of contribution include:
- Implementing additional Flask features.
- Expanding Discord bot functionalities (commands, event listeners, etc.).
- Integrating new third-party APIs or services.
- Improving the MVC structures
  
Check out the **issues** section for current needs, or suggest your own enhancements!

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MahediZaber51/MVC-Python.git
   cd MVC-Python
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**:
   Create a `.env` file in the root directory with the required environment variables for Flask and Discord (check the `.env-example` file).

4. **Run the Application**:
   ```bash
   python config/boot.py
   ```

5. **Run in Docker**:
   ```bash
   docker build -t flask-discord-app .
   docker run -d -p 5000:5000 flask-discord-app
   ```

## License

This project is licensed under the GNU General Public License v3.0.
