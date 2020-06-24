# Jak to przeżyć
1. Pisz szybko, edytuj powoli. Zdanie to zdanie, nie musi być od razu idealne i dopieszczone.
2. Budowanie:
```
pdflatex Praca_magisterska.tex
bibtex Praca_magisterska.aux
pdflatex Praca_magisterska.tex
pdflatex Praca_magisterska.tex
```
(zawarte też w skrypcie build.sh)

Przygotowanie danych testowych z http://dlib.net/files/data/:
1. Pobrano dlib_face_detector_training_data.tar.gz, wypakowano
2. Wyjęte wszystkie pliki z podfolderów do jednego folderu. Do podfolderu sunglasses wrzucono zdjęcia osób, które miały na twarzy ciemne okulary uniemożliwiające zobaczenie oczu.
3. Korzystając ze script.py wyjęto z pliku frontal_faces.xml nazwy plików do pliku image_names_frontal.txt.
4. Korzystając ze script.py wyjęto z pliku left_faces.xml nazwy plików do pliku image_names_left.txt
5. Nazwy zostały użyte na zbiorze plików, żeby wyrzucić te, których wg README w ogóle nie powinno tam być (wat).