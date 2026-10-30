import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def gerar_curadoria_filmes(dados_filmes):
    print(" Processando dados e gerando insights de cinema com IA...")

    prompt = (
        "Você é um crítico de cinema sênior e especialista em curadoria de dados de entretenimento. "
        "Com base na lista de filmes fornecida abaixo, elabore um relatório de curadoria estruturado "
        "contendo: 1) Destaque da Semana, 2) Perfil ideal para cada filme, e 3) Uma recomendação rápida "
        "em tópicos, com uma linguagem fluida e profissional."
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Filmes coletados: {dados_filmes}"}
        ],
        model="openai/gpt-oss-120b",
        temperature=0.4,
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
  
    filmes_coletados = [
        {"titulo": "Interestelar", "genero": "Ficção Científica / Drama", "nota": "8.7", "tema": "Viagem espacial e tempo"},
        {"titulo": "A Origem", "genero": "Suspense / Sci-Fi", "nota": "8.8", "tema": "Sonhos e espionagem industrial"},
        {"titulo": "O Poderoso Chefão", "genero": "Crime / Drama", "nota": "9.2", "tema": "Máfia e dinâmica familiar"}
    ]

    relatorio_cinema = gerar_curadoria_filmes(filmes_coletados)
    print("\n--- RELATÓRIO DE CURADORIA DE CINEMA ---")
    print(relatorio_cinema)