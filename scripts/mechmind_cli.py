#!/usr/bin/env python3
"""
CLI Principal de MechanicalMind AI - Versión Aprendizaje
"""

import click
import datetime
import sys
import os

# Añadir el path para importar nuestros módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from mechanicalmind_ai.core.analyzer import DependencyAnalyzer, ErrorDiagnosisEngine
    ADVANCED_MODE = True
except ImportError:
    ADVANCED_MODE = False

@click.group()
def cli():
    """MechanicalMind AI - Sistema de Gestión de Dependencias"""
    pass

@cli.command()
@click.argument('error_message')
def diagnose(error_message):
    """Diagnostica un error de dependencias"""
    
    if ADVANCED_MODE:
        # Modo avanzado con el motor de IA
        engine = ErrorDiagnosisEngine()
        result = engine.diagnose(error_message)
    else:
        # Modo básico (fallback)
        result = {
            "error_type": error_message.split(":")[0] if ":" in error_message else "UnknownError",
            "solutions": [
                "Ejecutar: pip install nombre_del_modulo_faltante",
                "Verificar el archivo requirements.txt",
                "Revisar mayúsculas/minúsculas en los imports",
                "Ejecutar: pip install --upgrade pip"
            ],
            "confidence": 0.7
        }
    
    click.echo("\n" + "="*50)
    click.echo("🔧 MECHANICALMIND AI - DIAGNÓSTICO")
    click.echo("="*50)
    click.echo(f"📋 Error: {error_message}")
    click.echo(f"🔍 Tipo: {result['error_type']}")
    click.echo(f"💪 Confianza: {result['confidence']*100:.1f}%")
    click.echo("\n💡 Soluciones recomendadas:")
    for i, solution in enumerate(result['solutions'], 1):
        click.echo(f"  {i}. {solution}")
    click.echo(f"\n🕐 Análisis realizado: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    click.echo("="*50)

@cli.command()
@click.argument('requirements_file', default='requirements.txt')
def analyze(requirements_file):
    """Analiza un archivo de dependencias"""
    
    if ADVANCED_MODE:
        analyzer = DependencyAnalyzer()
        result = analyzer.analyze(requirements_file)
        # Asegurar que el resultado tenga la clave file_analyzed
        result['file_analyzed'] = requirements_file
    else:
        # Modo básico mejorado
        result = {
            "status": "basic_analysis",
            "file_analyzed": requirements_file,
            "issues": ["Análisis básico - Modo de aprendizaje activado"],
            "recommendations": [
                "Implementar análisis de compatibilidad en próximas versiones",
                "Agregar detección de vulnerabilidades de seguridad",
                "Incluir verificación de versiones obsoletas"
            ]
        }
    
    click.echo("\n" + "="*50)
    click.echo("📊 MECHANICALMIND AI - ANÁLISIS")
    click.echo("="*50)
    click.echo(f"📁 Archivo: {result['file_analyzed']}")
    click.echo(f"📊 Estado: {result['status']}")
    
    if result.get('issues'):
        click.echo("\n⚠️  Issues detectados:")
        for issue in result['issues']:
            click.echo(f"  • {issue}")
    
    if result.get('recommendations'):
        click.echo("\n💡 Recomendaciones:")
        for rec in result['recommendations']:
            click.echo(f"  • {rec}")
    
    click.echo("="*50)

@cli.command()
def version():
    """Muestra la versión del sistema"""
    click.echo("🛠️ MechanicalMind AI v0.1.0 - Modo Aprendizaje")
    click.echo("📚 Sistema de gestión de dependencias educativo")
    click.echo("🚀 Desarrollado por mechmind-dwv")

if __name__ == '__main__':
    cli()
