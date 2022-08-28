<template>
    <div>
        <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
    </div>
</template>

<script>
export default {
    props: ['uc'],
    data() {
        return {
            data: [],
            layout: {
                title: "Precipitação (mm) durante o Ano",
            },
        };
    },
    async mounted() {

        //const response = await this.$axios.$get(`/getPrecipitacao?cod_uc=${this.cod_uc}&ano=${this.ano}`);
        const response = await this.$axios.$get(`/getPrecipitacao?cod_uc=0000.00.0003&ano=2020`);

        this.data.push(response)
    },
};
</script>

<style>
</style>