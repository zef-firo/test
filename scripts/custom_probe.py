"""Nodo dimostrativo: genera una singola riga per testare dynamic_code."""

import pyarrow as pa


def get_output_schema():
    return pa.schema([
        pa.field("message", pa.string()),
        pa.field("source", pa.string()),
    ])


def on_startup():
    return pa.RecordBatch.from_pydict(
        {
            "message": ["Dynamic code eseguito correttamente"],
            "source": ["custom_probe.py"],
        },
        schema=get_output_schema(),
    )
