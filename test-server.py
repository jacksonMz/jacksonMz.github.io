"""
Servidor HTTP simple para probar el frontend con el chatbot integrado
"""
import http.server
import socketserver
import os
import urllib.parse
import json

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_POST(self):
        # Simular API del chatbot para pruebas
        if self.path.startswith('/api/chatbot/'):
            self.handle_chatbot_api()
        else:
            super().do_POST()
    
    def do_GET(self):
        # Manejar requests de API del chatbot
        if self.path.startswith('/api/chatbot/'):
            self.handle_chatbot_api()
        else:
            super().do_GET()
    
    def handle_chatbot_api(self):
        """Simular respuestas de la API del chatbot para pruebas"""
        
        if self.path == '/api/chatbot/health':
            response = {
                "success": True,
                "data": {
                    "status": "active",
                    "message": "Chatbot funcionando (modo demo)",
                    "ai_enabled": True,
                    "timestamp": "2025-09-06T04:44:10.756031"
                }
            }
        
        elif self.path == '/api/chatbot/suggestions':
            response = {
                "success": True,
                "data": {
                    "sugerencias": [
                        "¿Cuáles son los horarios de salida?",
                        "¿Qué rutas tienen disponibles?",
                        "¿Cuánto cuestan los pasajes?",
                        "¿Cómo puedo hacer una reserva?",
                        "¿Qué servicios ofrecen en los buses?",
                        "Información de contacto"
                    ]
                }
            }
        
        elif self.path == '/api/chatbot/message':
            # Leer el mensaje del POST
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                mensaje = data.get('mensaje', '').lower()
                
                # Respuestas simuladas
                if 'hola' in mensaje or 'buenas' in mensaje:
                    bot_response = "¡Hola! 👋 Soy el asistente virtual de Transporte Serrano del Oriente. ¿En qué puedo ayudarte?"
                elif 'horarios' in mensaje:
                    bot_response = "🕐 Nuestros horarios de salida son:\n• Primer bus: 5:00 AM\n• Salidas frecuentes cada 30 minutos\n• Último bus: 10:00 PM"
                elif 'precio' in mensaje or 'costo' in mensaje:
                    bot_response = "💰 Nuestras tarifas varían según el destino:\n• Rutas urbanas: $2.000 - $3.500\n• Rutas interurbanas: $5.000 - $15.000"
                elif 'rutas' in mensaje:
                    bot_response = "🗺️ Nuestras principales rutas incluyen:\n• Ciudad A ↔ Ciudad B\n• Ciudad A ↔ Ciudad C\n• Rutas locales urbanas"
                elif 'reserv' in mensaje:
                    bot_response = "🎫 Para hacer reservas puedes:\n• Usar nuestra aplicación móvil\n• Visitar nuestras oficinas\n• Llamar por teléfono"
                else:
                    bot_response = "🤔 Esta es una respuesta de prueba. En producción, el chatbot con IA procesaría tu mensaje correctamente."
                
                response = {
                    "success": True,
                    "data": {
                        "respuesta": bot_response,
                        "categoria": "demo",
                        "confianza": 0.85,
                        "timestamp": "2025-09-06T04:44:10.756031",
                        "usuario": "Demo"
                    }
                }
            except:
                response = {
                    "success": False,
                    "message": "Error procesando mensaje",
                    "code": "DEMO_ERROR"
                }
        
        else:
            response = {
                "success": False,
                "message": "Endpoint no encontrado",
                "code": "NOT_FOUND"
            }
        
        # Enviar respuesta
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))

if __name__ == "__main__":
    PORT = 8080
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🌐 Servidor de prueba ejecutándose en: http://localhost:{PORT}")
        print(f"📁 Directorio: {os.getcwd()}")
        print(f"🤖 API de chatbot simulada habilitada")
        print(f"🔗 Prueba el sistema en: http://localhost:{PORT}/index.html")
        print("\n💡 Endpoints simulados:")
        print("  - GET  /api/chatbot/health")
        print("  - GET  /api/chatbot/suggestions") 
        print("  - POST /api/chatbot/message")
        print("\nPresiona Ctrl+C para detener el servidor")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor detenido")
