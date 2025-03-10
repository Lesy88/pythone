import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Carica il file CSV
df = pd.read_csv('Students_Grading_Dataset.csv')
print("\n--- df.head: --- \n",df.head())
print("--- info: --- \n", df.info())
print("\n--- df.describe: --- \n",df.describe())

#4.Separazione tra Colonne Numeriche e Categoriali
colonne_numeriche = df.select_dtypes(include=[np.number]).columns.tolist()
colonne_categoriali = df.select_dtypes(include=['object']).columns.tolist()
print("Colonne numeriche:", colonne_numeriche)
print("Colonne categoriali:", colonne_categoriali)

#5.Identificazione e Conteggio dei Valori Mancanti (NaN)
valori_mancanti = df.isna().sum()
# Visualizza i risultati
print(valori_mancanti)

#6.Sostituire i NaN nelle colonne numeriche con la mediana corrispondente.
for col in colonne_numeriche:
    mediana = df[col].median()  # Calcola la mediana della colonna
    df[col].fillna(mediana, inplace=True)  # Sostituisci i NaN con la mediana


df['Parent_Education_Level'].fillna('Undefined', inplace=True)

# Verifica che i valori NaN siano stati sostituiti
print(df['Parent_Education_Level'].isna().sum())

df.to_csv("Students_senzaUndef.csv",index=False)


#Creare un grafico a barre per visualizzare la distribuzione Department

department_counts = df['Department'].value_counts()
#department_counts = df['Parent_Education_Level'].value_counts()
# Crea il grafico a barre orizzontale
plt.barh(department_counts.index, department_counts.values)
# Aggiungi etichette e titolo
plt.xlabel("Conteggio")
plt.ylabel("Categorie")
plt.title("Distribuzione dei Dipartimenti")
plt.ylabel('')
plt.tight_layout()
plt.savefig('distribuzione_department.png')
# Mostra il grafico
plt.show()



#Distribuzione degli Studenti per Ore di Studio Settimanali
study_hours_counts = df['Study_Hours_per_Week'].value_counts().sort_index()
# Crea il grafico a barre
plt.bar(study_hours_counts.index, study_hours_counts.values, color='b')
# Aggiungi etichette agli assi e titolo
plt.xlabel("Ore di Studio per Settimana")
plt.ylabel("Numero di Studenti")
plt.title("Distribuzione degli Studenti per Ore di Studio Settimanali")
# Mostra il grafico
plt.show()

#9.Box Plot per Analisi della Distribuzione
plt.figure(figsize=(8, 6))
sns.boxplot(x='Stress_Level (1-10)', y='Final_Score', data=df, palette='Set2')
# Aggiungi etichette e titolo
plt.xlabel("Stress_Level (1-10)")
plt.ylabel("Final Score")
plt.title("Box Plot della Distribuzione del Final Score per Genere")
# Mostra il grafico
plt.show()

#10.Scatter Plot per Analisi di Correlazione
plt.figure(figsize=(8, 6))
# Utilizza seaborn per creare il grafico a dispersione
sns.scatterplot(x='Sleep_Hours_per_Night', y='Attendance (%)', data=df, color='b', marker='o')
# Aggiungi etichette e titolo
plt.xlabel("Ore di Sonno per Notte")
plt.ylabel("Percentuale di Presenza")
plt.title("Scatter Plot: Relazione tra Ore di Sonno e Percentuale di Presenza")
# Mostra il grafico
plt.show()

#11.Creare una heatmap per visualizzare la matrice di correlazione tra le variabili del DataFrame
# Crea la heatmap della matrice di correlazione
correlation_matrix = df.corr(numeric_only=True)

# Crea la heatmap della matrice di correlazione
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, square=True, cbar_kws={'shrink': 0.75})
# Aggiungi titolo
plt.title("Matrice di Correlazione tra le Variabili")
# Mostra il grafico
plt.show()

#12.una pivot table che mostri la media della colonna "Projects_Score" per ciascun valore della colonna "Gender"
pivot_table = df.pivot_table(values='Projects_Score', index='Gender', aggfunc='mean')
# Visualizza la pivot table
print(pivot_table)
#13. Calcola la distribuzione percentuale della colonna "Age"
age_counts = df['Age'].value_counts()
# Crea il grafico a torta
plt.figure(figsize=(8, 6))
plt.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightyellow'])
# Aggiungi titolo
plt.title('Distribuzione Percentuale per la Colonna Age')
# Mostra il grafico
plt.show()

#14.Distribuzione degli Studenti per Ore di Studio Settimanali
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
# Aggiungi etichette e titolo
plt.xlabel("Età")
plt.ylabel("Frequenza")
plt.title("Distribuzione delle Età")
# Mostra il grafico
plt.show()

#15.Pair Plot per Esplorare le Relazioni
sns.pairplot(df[['Final_Score', 'Attendance (%)','Midterm_Score']])
# Aggiungi titolo
plt.suptitle("Pair Plot tra Final Score e Attendance (%)", y=1.02)
# Mostra il grafico
plt.show()

#16.Grafici Multipli (Subplot) per Confronti
# Imposta la figura con 2 sottogruppi (1 colonna, 2 righe)
plt.figure(figsize=(10, 8))
# Primo grafico (Assignments_Avg)
plt.subplot(2, 1, 1)  # (nrows, ncols, index)
plt.plot(df['Assignments_Avg'], color='skyblue', label='Assignments Avg')
plt.xlabel('Studenti')
plt.ylabel('Assignments Avg')
plt.title('Andamento dei Punteggi Medi degli Assignments')
plt.legend()
# Secondo grafico (Final_Score)
plt.subplot(2, 1, 2)  # (nrows, ncols, index)
plt.plot(df['Final_Score'], color='lightgreen', label='Final Score')
plt.xlabel('Studenti')
plt.ylabel('Final Score')
plt.title('Andamento dei Punteggi Finali')
plt.legend()
# Aggiungi uno spazio tra i grafici per evitare sovrapposizioni
plt.tight_layout()
# Mostra il grafico
plt.show()

#17.Grafico a Barre Orizzontali
income_counts = df['Family_Income_Level'].value_counts()
# Crea il grafico a barre orizzontali
plt.figure(figsize=(10, 6))
income_counts.plot(kind='barh', color='skyblue', edgecolor='black')
# Aggiungi etichette e titolo
plt.xlabel('Conteggio')
plt.ylabel('Livello di Reddito Familiare')
plt.title('Distribuzione del Livello di Reddito Familiare')
# Mostra il grafico
plt.show()

#17.Grafico ad Area per Trend Cumulativi
# Calcola la somma cumulativa della colonna "Stress_Level"
df['Cumulative_Stress'] = df['Stress_Level (1-10)'].cumsum()
# Crea il grafico ad area
plt.figure(figsize=(10, 6))
plt.fill_between(df.index, df['Cumulative_Stress'], color='skyblue', alpha=0.4)
# Aggiungi etichette e titolo
plt.xlabel('Indice')
plt.ylabel('Stress Cumulativo')
plt.title('Andamento Cumulativo dello Stress nel Tempo')
# Mostra il grafico
plt.show()

#18.Grafico a Bolle per Relazioni Multidimensionali

plt.figure(figsize=(10, 6))
# Crea il grafico a bolle
bubble = plt.scatter(df['Final_Score'], df['Sleep_Hours_per_Night'], 
                     s=df['Final_Score']*0.7,  # Dimensione delle bolle proporzionale al 'Final_Score' (multiplicato per un fattore per visibilità)
                     c=df['Sleep_Hours_per_Night'],  # Colore delle bolle basato su 'Sleep_Hours_per_Night'
                     cmap='viridis',  # Mappa di colori
                     alpha=0.6,  # Trasparenza delle bolle
                     edgecolors="w",  # Bordo bianco per le bolle
                     linewidth=1)

# Aggiungi barra dei colori
plt.colorbar(bubble, label='Sleep Hours per Night')
# Etichette e titolo
plt.xlabel('Final Score')
plt.ylabel('Sleep Hours per Night')
plt.title('Grafico a Bolle tra Final Score e Sleep Hours per Night')
# Mostra il grafico
plt.show()
