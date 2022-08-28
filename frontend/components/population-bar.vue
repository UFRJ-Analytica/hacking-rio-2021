<template>
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
</template>

<script>
export default {
    data() {
        return {
            data: [],
            layout: {
                xaxis: {
                    type: 'category',
                    title: 'Id',
                },
                title: "My graph",
            },
        };
    },
    async mounted() {

        const response = await this.$axios.$get("/pop/10?year=2020");
        console.log(response)
        console.log(this)
        this.data.push(response)
    },
}
</script>

<style>

</style>