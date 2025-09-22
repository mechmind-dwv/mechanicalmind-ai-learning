#!/bin/bash
echo "🚀 Instalando MechanicalMind AI - Modo Aprendizaje"

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install --upgrade pip
pip install -e .

echo "✅ Instalación completada!"
echo ""
echo "💻 Para usar el sistema:"
echo "   source venv/bin/activate"
echo "   mechmind --help"
