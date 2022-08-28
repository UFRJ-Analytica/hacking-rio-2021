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
                xaxis: {
                    type: 'category',
                    title: 'Id',
                },
                title: "Áreas queimadas (km2) por ano",
            },
        };
    },
    async mounted() {

        const response = await this.$axios.$get(`/getQueimadasData?uc=${this.uc}`);

        this.data.push(response)
    },
};
</script>

<style>
</style>