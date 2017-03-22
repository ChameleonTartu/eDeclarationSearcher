# eDeclarationSearcher
Repository for search in Ukrainian digital declaration API.

# Motivation behind the project
I hate software which is badly designed and not easy to use. Therefore, I have created my own search which communicats with https://public-api.nazk.gov.ua/v1/declaration/ API, which has problems with unicode in browsers and in general quite hard to use for regular people. Doing this project I also want to help my family to track their declarations.

# Problems
I have designed this project in less than 8 hours. Therefore, it is quite slow and have limitations, for example it is not possible to see all people from the database. Onе more reason, API itself allows to get no more than 400 people/request. Currently, in the database more than 700,000 people so it may take several hours to fetch data simultaneously. There is no filters, sortings or anything similar, but if project proves it is usefulness, I will definitely add all this functionality. 

# Пошуковик в електронній базі декларацій
Цей проект створений для спрощення взаємодії людей з українською базою електронних декларацій.

# Мотивація щодо створення цього проекту
Я терпіти не можу погані проагмні продукти, котрі окрім того, що погано спроектовані, також важко використовувати. Тому, я створив мій власний пошуковик, який взаємодіє з https://public-api.nazk.gov.ua/v1/declaration/ АPI для отримання даних. Головні проблеми API - некоректне відображженя unicode символів в браузері, а також, загалом, не можливість використання звичайними людьми. Створюючи цей проект, я хотів би допомогти моїй родині контролювати подані декларації.

# Проблеми
Я створив цей проект за менше, ніж 8 годин. Тому, пошуковик працює досить повільно, також неможливо отримати звіт по всім людям в базі, частково це тому, що на час написання цього продукту в базі було більше 700000 людей, тому це може зайняти декілька годин, щоб отримати всі дані(якщо отримувати їх послідовно), також API саме по собі не дозволяє отримати більше 400 людей за один раз(якщо я правильно зрозумів, адже документація відрізняється від даних, які я отримую). На разі, немає жодних фільтрів, сортувань або чохось схожого, але якщо проект знайде свою аудиторію, то я додам усі необхідні функції.
