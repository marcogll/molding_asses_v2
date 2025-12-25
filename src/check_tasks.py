#!/usr/bin/env python3
"""
Verificador y Ejecutor de Tareas del Roadmap de Code Carol
Lee TASKS.md y ejecuta las tareas pendientes de forma interactiva
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple


class TaskManager:
    """Gestor de tareas del roadmap"""
    
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.tasks_file = base_path / "TASKS.md"
        self.tasks = self.parse_tasks()
    
    def parse_tasks(self) -> List[Dict]:
        """Lee TASKS.md y extrae todas las tareas"""
        with open(self.tasks_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tasks = []
        current_phase = None
        
        # Regex para detectar fases y tareas
        phase_pattern = r'^## (Fase \d+: .+)$'
        task_pattern = r'^- \[(.)\] \*\*(.+?)\*\*'
        subtask_pattern = r'^\s+- \[(.)\] (.+)$'
        
        lines = content.split('\n')
        current_task = None
        
        for line in lines:
            # Detectar fase
            phase_match = re.match(phase_pattern, line)
            if phase_match:
                current_phase = phase_match.group(1)
                continue
            
            # Detectar tarea principal
            task_match = re.match(task_pattern, line)
            if task_match:
                status = task_match.group(1)
                name = task_match.group(2)
                
                current_task = {
                    'phase': current_phase,
                    'name': name,
                    'status': 'done' if status == 'x' else 'pending',
                    'subtasks': []
                }
                tasks.append(current_task)
                continue
            
            # Detectar subtarea
            subtask_match = re.match(subtask_pattern, line)
            if subtask_match and current_task:
                sub_status = subtask_match.group(1)
                sub_name = subtask_match.group(2)
                
                current_task['subtasks'].append({
                    'name': sub_name,
                    'status': 'done' if sub_status == 'x' else 'pending'
                })
        
        return tasks
    
    def get_phase_summary(self) -> Dict[str, Dict]:
        """Genera resumen por fase"""
        summary = {}
        
        for task in self.tasks:
            phase = task['phase']
            if not phase:
                continue
            
            if phase not in summary:
                summary[phase] = {
                    'total_tasks': 0,
                    'completed_tasks': 0,
                    'total_subtasks': 0,
                    'completed_subtasks': 0
                }
            
            summary[phase]['total_tasks'] += 1
            if task['status'] == 'done':
                summary[phase]['completed_tasks'] += 1
            
            for subtask in task['subtasks']:
                summary[phase]['total_subtasks'] += 1
                if subtask['status'] == 'done':
                    summary[phase]['completed_subtasks'] += 1
        
        return summary
    
    def print_status(self):
        """Imprime estado actual de todas las fases"""
        print("\n" + "=" * 70)
        print("📊 ESTADO DEL ROADMAP - CODE CAROL")
        print("=" * 70 + "\n")
        
        summary = self.get_phase_summary()
        
        for phase, stats in summary.items():
            total = stats['total_subtasks'] if stats['total_subtasks'] > 0 else stats['total_tasks']
            completed = stats['completed_subtasks'] if stats['total_subtasks'] > 0 else stats['completed_tasks']
            
            percentage = (completed / total * 100) if total > 0 else 0
            
            # Barra de progreso
            bar_length = 30
            filled = int(bar_length * completed / total) if total > 0 else 0
            bar = '█' * filled + '░' * (bar_length - filled)
            
            # Emoji de estado
            if percentage == 100:
                emoji = "✅"
            elif percentage > 0:
                emoji = "🚧"
            else:
                emoji = "⚪"
            
            print(f"{emoji} {phase}")
            print(f"   [{bar}] {percentage:.1f}% ({completed}/{total})")
            print()
    
    def get_pending_tasks(self) -> List[Dict]:
        """Obtiene lista de tareas pendientes"""
        pending = []
        
        for task in self.tasks:
            if task['status'] == 'pending':
                # Si tiene subtareas, solo agregar las pendientes
                if task['subtasks']:
                    pending_subtasks = [st for st in task['subtasks'] if st['status'] == 'pending']
                    if pending_subtasks:
                        pending.append({
                            'phase': task['phase'],
                            'task': task['name'],
                            'subtasks': pending_subtasks
                        })
                else:
                    pending.append({
                        'phase': task['phase'],
                        'task': task['name'],
                        'subtasks': []
                    })
        
        return pending
    
    def print_next_steps(self):
        """Imprime próximas tareas a realizar"""
        pending = self.get_pending_tasks()
        
        if not pending:
            print("🎉 ¡Todas las tareas completadas!")
            return
        
        print("\n" + "=" * 70)
        print("🎯 PRÓXIMAS TAREAS PENDIENTES")
        print("=" * 70 + "\n")
        
        for idx, item in enumerate(pending[:5], 1):  # Mostrar solo las primeras 5
            print(f"{idx}. [{item['phase']}]")
            print(f"   📌 {item['task']}")
            
            if item['subtasks']:
                for subtask in item['subtasks']:
                    print(f"      - {subtask['name']}")
            print()
    
    def suggest_commands(self):
        """Sugiere comandos para ejecutar tareas pendientes"""
        print("\n" + "=" * 70)
        print("💡 COMANDOS SUGERIDOS")
        print("=" * 70 + "\n")
        
        pending = self.get_pending_tasks()
        
        if not pending:
            return
        
        # Detectar qué fase está pendiente y sugerir comandos
        for item in pending[:3]:
            phase = item['phase']
            task = item['task']
            
            # Fase 2: Traducción
            if 'Fase 2' in phase:
                if 'Inglés' in task or 'EN' in task:
                    print("🇺🇸 Traducción al Inglés:")
                    print("   # Probar con muestra pequeña")
                    print("   python src/test_translation.py")
                    print()
                    print("   # Traducción completa")
                    print("   python src/translate_with_ai.py --lang en")
                    print()
                
                elif 'Francés' in task or 'FR' in task:
                    print("🇫🇷 Traducción al Francés:")
                    print("   python src/translate_with_ai.py --lang fr")
                    print()
                
                elif 'Portugués' in task or 'BR' in task:
                    print("🇧🇷 Traducción al Portugués Brasileño:")
                    print("   python src/translate_with_ai.py --lang br")
                    print()
                
                elif 'Chino' in task or 'CN' in task:
                    print("🇨🇳 Traducción al Chino Simplificado:")
                    print("   python src/translate_with_ai.py --lang cn")
                    print()
                
                elif 'Alemán' in task or 'GE' in task:
                    print("🇩🇪 Traducción al Alemán:")
                    print("   python src/translate_with_ai.py --lang ge")
                    print()
            
            # Fase 3: Web Server
            elif 'Fase 3' in phase:
                if 'Setup del Servidor' in task:
                    print("🚀 Setup del Web Server:")
                    print("   # Opción 1: FastAPI")
                    print("   pip install fastapi uvicorn sqlalchemy")
                    print("   mkdir -p backend/{models,routes,services}")
                    print()
                    print("   # Opción 2: Flask")
                    print("   pip install flask flask-sqlalchemy flask-cors")
                    print("   mkdir -p app/{models,routes,services}")
                    print()
                
                elif 'Base de Datos' in task:
                    print("🗄️  Setup de Base de Datos:")
                    print("   # SQLite para desarrollo")
                    print("   pip install sqlalchemy alembic")
                    print()
                    print("   # PostgreSQL para producción")
                    print("   pip install psycopg2-binary")
                    print()
            
            # Fase 4: Frontend
            elif 'Fase 4' in phase:
                print("🎨 Setup de Frontend:")
                print("   # Next.js")
                print("   npx create-next-app@latest frontend")
                print()
                print("   # React + Vite")
                print("   npm create vite@latest frontend -- --template react-ts")
                print()
            
            # Fase 5: Deployment
            elif 'Fase 5' in phase:
                if 'Docker' in task:
                    print("🐳 Dockerización:")
                    print("   # Crear Dockerfile")
                    print("   touch Dockerfile docker-compose.yml")
                    print()


def main():
    """Función principal"""
    base_path = Path(__file__).parent.parent
    
    manager = TaskManager(base_path)
    
    # Imprimir estado
    manager.print_status()
    
    # Imprimir próximos pasos
    manager.print_next_steps()
    
    # Sugerir comandos
    manager.suggest_commands()
    
    print("\n" + "=" * 70)
    print("📚 Documentación Útil:")
    print("=" * 70)
    print("  - Guía de Traducción: docs/TRANSLATION_GUIDE.md")
    print("  - Estado del Proyecto: docs/PROJECT_STATUS.md")
    print("  - Roadmap Completo: TASKS.md")
    print()


if __name__ == "__main__":
    main()
