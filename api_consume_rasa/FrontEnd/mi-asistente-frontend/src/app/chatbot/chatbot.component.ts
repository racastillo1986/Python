import {Component, ViewChild, ElementRef, AfterViewInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {
  trigger,
  style,
  transition,
  animate
} from '@angular/animations';

// AfterViewInit -> sirve para correr código justo después de que el HTML esté listo para usarse
@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrl: './chatbot.component.css',
  animations: [
    trigger('fadeInUp', [
      transition(':enter', [
        style({opacity: 0, transform: 'translateY(10px)'}),
        animate('300ms ease-out', style({opacity: 1, transform: 'translateY(0)'}))
      ])
    ])
  ]
})
export class ChatbotComponent implements AfterViewInit {

  @ViewChild('scrollContainer') scrollContainer!: ElementRef;


  mensaje: string = '';
  mensajes: { tipo: 'usuario' | 'bot', texto: string }[] = [];

  private autoScroll = true;

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

  constructor(private http: HttpClient) {
  }

  objectKeys = Object.keys;

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


  enviarMensaje() {
    if (this.mensaje.trim()) {
      this.mensajes.push({tipo: 'usuario', texto: this.mensaje});
      this.scrollToBottom();

      const payload = {
        sender: 'usuario123',
        message: this.mensaje
      };

      // mensaje temporal del bot
      this.mensajes.push({tipo: 'bot', texto: 'Estoy pensando 🤖...'});
      this.scrollToBottom();

      this.http.post<any[]>('http://localhost:8080/asistente/mensaje', payload).subscribe({
        next: (respuestas) => {
          // quitar el mensaje temporal
          this.mensajes.pop();

          respuestas.forEach(res => {
            this.mensajes.push({tipo: 'bot', texto: res.text});
            this.scrollToBottom();
          });
        },
        error: (error) => {
          this.mensajes.pop(); // quita el "Estoy pensando 🤖..."
          console.error('❌ Error al comunicar con el backend:', error);
          this.mensajes.push({tipo: 'bot', texto: '❌ Error al conectar con el asistente.'});
          this.scrollToBottom();
        }
      });

      this.mensaje = '';
    }
  }
}
