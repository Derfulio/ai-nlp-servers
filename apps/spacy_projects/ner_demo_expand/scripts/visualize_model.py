import spacy_streamlit
import typer
import spacy


def main(models: str, default_text: str):
    models = [name.strip() for name in models.split(",")]
    # In order to have the list of all available labels from all the pipeline elements of type ner, we need to list them.
    ner_labels = ()
    for model in models:
        nlp = spacy.load(model)
        pipe_factories = nlp.pipe_factories
        for pipe_name in pipe_factories:
            if str(pipe_factories[pipe_name]) == "ner":
                ner_labels += nlp.get_pipe(pipe_name).labels
    ner_labels = tuple(set(ner_labels))
    spacy_streamlit.visualize(models, default_text, visualizers=["ner"], ner_labels=ner_labels)


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass
