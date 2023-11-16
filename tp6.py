import pandas as pd

df = pd.read_csv('titanic.csv')

# Exo1 Affichez les données dans la console
# print(df.head())

# Exo2 Affichez l’âge moyen de tous les passagers, puis l’âge minimum et l’âge maximum.
# Indice : Utilisez les fonctions mean(), min(), et max().

print('Average age: ', df['Age'].mean())
print('Min age: ', df['Age'].min())
print('Max age: ', df['Age'].max())

# Exo3 Triez les passagers par Age croissant.
# Indice : Utilisez df[df['Age'].notna()] pour supprimer les valeurs nulles

# print(df[df['Age'].notna()].sort_values(by=['Age']))

# Exo4 Créez un nouveau tableau qui ne contient que l’identifiant et le nom des hommes qui ont payé plus de 10$.
# print(df[df['Fare'] > 10][['PassengerId', 'Name']])

# Exo5 Supprimez tous les passagers de la 3ème classe.
# print(df[df['Pclass'] != 3])

# Exo6 Pour chaque sexe, afficher l’âge moyen, et le prix de billet moyen.
# Indice : Utilisez groupby()
print('F average age: ', (df[df['Sex'] == 'female']['Age']).mean())
print('M average age: ', (df[df['Sex'] == 'male']['Age']).mean())
print('F average price: ', (df[df['Sex'] == 'female']['Fare']).mean())
print('M average price: ', (df[df['Sex'] == 'male']['Fare']).mean())

print(df.groupby(['Sex'])[['Age', 'Fare']].mean())

# Exo7 Pour chaque sexe et chaque classe de billet, afficher l’âge moyen, et le prix de billet moyen.
print(df.groupby(['Sex', 'Pclass'])[['Age', 'Fare']].mean())

# Exo8 Remplacez tous les noms des passagers par leur nom en majuscule.
# Indice : Utilisez la fonction str.upper()
df['Name'] = df['Name'].map(lambda x: x.upper())
# print(df)

# Exo9 Ajoutez une nouvelle colonne dans le dataframe, qui contient la valeur « Retraité » si le passager a plus de 65 ans, « En activité » sinon.
# Indice : Utilisez la fonction apply()
def is_retired(age):
    if age > 65:
        return 'Retraité'
    else:
        return 'En activité'
df['Activité'] = df.apply(lambda x: is_retired(x['Age']), axis=1)
print(df[df['Activité'] == 'Retraité'])
