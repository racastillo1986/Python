import { Component, ViewChild, ElementRef, AfterViewInit, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import {
  trigger,
  style,
  transition,
  animate
} from '@angular/animations';

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrl: './chatbot.component.css',
  animations: [
    trigger('fadeInUp', [
      transition(':enter', [
        style({ opacity: 0, transform: 'translateY(10px)' }),
        animate('300ms ease-out', style({ opacity: 1, transform: 'translateY(0)' }))
      ])
    ])
  ]
})
export class ChatbotComponent implements AfterViewInit, OnInit {

  @ViewChild('scrollContainer') scrollContainer!: ElementRef;

  mensaje: string = '';
  mensajes: { tipo: 'usuario' | 'bot', texto: string, hora: string }[] = [];

  private autoScroll = true;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    const historial = localStorage.getItem('historialChat');
    if (historial) {
      this.mensajes = JSON.parse(historial);
    } else {
      this.mensajes.push({
        tipo: 'bot',
        texto: '¡Hola! 😊 ¿En qué puedo ayudarte hoy?',
        hora: this.obtenerHora()
      });
      this.guardarMensajesEnLocalStorage();
    }
  }

  ngAfterViewInit() {
    this.scrollContainer.nativeElement.addEventListener('scroll', () => {
      const element = this.scrollContainer.nativeElement;
      const atBottom = element.scrollHeight - element.scrollTop === element.clientHeight;
      this.autoScroll = atBottom;
    });
    this.scrollToBottom();
  }

  ngAfterViewChecked() {
    this.scrollToBottom();
  }

  objectKeys = Object.keys;

  obtenerHora(): string {
    return new Date().toLocaleString([], { dateStyle: 'short', timeStyle: 'short' });
  }

  isJson(texto: string): boolean {
    try {
      JSON.parse(texto);
      return true;
    } catch {
      return false;
    }
  }

  parseJson(texto: string): any[] {
    try {
      return JSON.parse(texto);
    } catch {
      return [];
    }
  }

  scrollToBottom(): void {
    if (this.autoScroll) {
      try {
        setTimeout(() => {
          this.scrollContainer.nativeElement.scroll({
            top: this.scrollContainer.nativeElement.scrollHeight,
            behavior: 'smooth'
          });
        }, 0);
      } catch (err) {
        console.error('Error en scroll:', err);
      }
    }
  }

  guardarMensajesEnLocalStorage() {
    localStorage.setItem('historialChat', JSON.stringify(this.mensajes));
  }

  enviarMensaje() {
    if (this.mensaje.trim()) {
      const horaActual = this.obtenerHora();
      this.mensajes.push({ tipo: 'usuario', texto: this.mensaje, hora: horaActual });
      this.guardarMensajesEnLocalStorage();
      this.scrollToBottom();

      const payload = {
        sender: 'usuario123',
        message: this.mensaje
      };

      // mensaje temporal del bot
      this.mensajes.push({ tipo: 'bot', texto: 'Estoy pensando 🤖...', hora: this.obtenerHora() });
      this.scrollToBottom();

      this.http.post<any[]>('http://localhost:8080/asistente/mensaje', payload).subscribe({
        next: (respuestas) => {
          this.mensajes.pop(); // quitar el "Estoy pensando 🤖..."
          respuestas.forEach(res => {
            this.mensajes.push({ tipo: 'bot', texto: res.text, hora: this.obtenerHora() });
            this.guardarMensajesEnLocalStorage();
            this.scrollToBottom();
          });
        },
        error: (error) => {
          this.mensajes.pop(); // quitar el "Estoy pensando 🤖..."
          console.error('❌ Error al comunicar con el backend:', error);
          this.mensajes.push({
            tipo: 'bot',
            texto: '❌ Error al conectar con el asistente.',
            hora: this.obtenerHora()
          });
          this.scrollToBottom();
        }
      });

      this.mensaje = '';
    }
  }

  borrarHistorial() {
    const confirmar = confirm('¿Estás seguro de que deseas borrar todo el historial?');
    if (!confirmar) return;

    this.mensajes = [];
    localStorage.removeItem('historialChat');

    // Mostrar mensaje sin guardarlo
    this.mensajes.push({
      tipo: 'bot',
      texto: '🗑️ Historial eliminado. ¡Empecemos de nuevo!',
      hora: this.obtenerHora()
    });

    // NOTA: No se llama a this.guardarMensajesEnLocalStorage()
    this.scrollToBottom();
  }
}
