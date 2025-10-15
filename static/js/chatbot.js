class Chatbot {
    constructor() {
        this.webhookUrl = 'https://n8n-ouap.onrender.com/webhook/3530726c-8be3-4d06-9477-fe14b77d3fd4';
        this.isOpen = false;
        this.init();
    }

    init() {
        this.bindEvents();
        this.addWelcomeMessage();
    }

    bindEvents() {
        const toggle = document.getElementById('chatbot-toggle');
        const close = document.getElementById('chatbot-close');
        const send = document.getElementById('chatbot-send');
        const input = document.getElementById('chatbot-input');

        toggle.addEventListener('click', () => this.toggleChat());
        close.addEventListener('click', () => this.closeChat());
        send.addEventListener('click', () => this.sendMessage());
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });
    }

    toggleChat() {
        const container = document.getElementById('chatbot-container');
        this.isOpen = !this.isOpen;
        container.style.display = this.isOpen ? 'flex' : 'none';
    }

    closeChat() {
        const container = document.getElementById('chatbot-container');
        this.isOpen = false;
        container.style.display = 'none';
    }

    addWelcomeMessage() {
        setTimeout(() => {
            this.addMessage('Hello! I\'m your AI assistant. How can I help you today?', 'bot');
        }, 500);
    }

    async sendMessage() {
        const input = document.getElementById('chatbot-input');
        const message = input.value.trim();
        
        if (!message) return;

        // Add user message
        this.addMessage(message, 'user');
        input.value = '';

        // Show typing indicator
        this.showTyping();

        try {
            const response = await fetch(this.webhookUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    timestamp: new Date().toISOString()
                })
            });

            // Remove typing indicator
            this.hideTyping();

            if (response.ok) {
                const data = await response.text();
                let botMessage;
                
                try {
                    const jsonData = JSON.parse(data);
                    botMessage = jsonData.response || jsonData.message || jsonData.reply || data;
                } catch {
                    botMessage = data || 'Response received';
                }
                
                this.addMessage(botMessage, 'bot');
            } else {
                this.addMessage(`Error: ${response.status} - ${response.statusText}`, 'bot');
            }

        } catch (error) {
            console.error('Chatbot error:', error);
            this.hideTyping();
            this.addMessage('Connection error. Please try again.', 'bot');
        }
    }

    addMessage(text, sender) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        messageDiv.textContent = text;
        
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    showTyping() {
        const messagesContainer = document.getElementById('chatbot-messages');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message typing';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = `
            <div class="typing-indicator">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        `;
        
        messagesContainer.appendChild(typingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    hideTyping() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new Chatbot();
});