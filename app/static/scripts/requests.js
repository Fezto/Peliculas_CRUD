axios.defaults.headers.common["X-CSRFToken"] = "{{ csrf_token() }}";

//* Retorna el cuerpo de una tabla como JSON
async function select_all(table) {
    const response = await axios.get(`/data/${table}/body`);
    return response.data;
}

//* Retorna las columnas de una tabla como JSON
async function select_columns(table) {
    const response = await axios.get(`/data/${table}/columns`);
    return response.data;
}

async function delete_from({table, id}) {
    await axios.delete(`/index/${table}/${id}`)
}