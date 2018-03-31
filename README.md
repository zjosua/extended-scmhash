# Extended Schema Hash for Anki

When Anki imports data from an .apkg file, it compares only the names and fields of models.
If the existing and imported collection have models with equal names and fields, Anki will assume they are the same, even if the models differ in another property, for example the 'css' property.
This addon extends the scope of model comparison.
