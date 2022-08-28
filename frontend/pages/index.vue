<template>
    <v-container>
        <h1>Tabela de Consulta das Unidades de Conservação</h1>
       <rankingTable></rankingTable>
       <br>
       <br>
       <h1>Mapa de Exibição</h1>
       <plotly-map></plotly-map>
    </v-container>
</template>

<script>
export default {
data() {
    return {
        tab_selector: false
    }
} 
}
</script>