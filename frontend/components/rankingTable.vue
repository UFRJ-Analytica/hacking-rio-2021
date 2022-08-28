<template>
  <div>
    <v-autocomplete
      auto-select-first
      chips
      clearable
      deletable-chips
      v-model="select"
      :items="items"
      @change="editTable"
      multiple
    ></v-autocomplete>
    <v-simple-table fixed-header height="300px">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Name</th>
            <th class="text-left">Indicador de Necessidade</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in data" :key="item.name">
            <td v-if="item.show">
              <NuxtLink :to="`uc/${item.name}`">{{ item.name }}</NuxtLink>
            </td>
            <td  v-if="item.show">{{ item.m1 }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      search: "",
      select: [],
      items: [],
      headers: [
        {
          text: "Unidades de Conservação",
          align: "start",
          sortable: false,
          value: "name",
        },
        {
          text: "Metric 1",
          align: "start",
          filterable: false,
          value: "m1",
        },
      ],
      data: [],
    };
  },
  methods: {
    editTable() {
        if(!this.select.length){
            this.data = this.data.map(item => {
                 item.show = true
                 return item
            })
        } else {
            this.data = this.data.map(item => {
                if(this.select.includes(item.name)){
                    item.show = true
                    console.log(item.name)
                } else {

                    item.show = false
                }
                return item
            })
        }
       
    },
  },
  async mounted() {
    const response = await this.$axios.$get("/getUCS");
    
    const indicators = await this.$axios.$get("/getIndicators");
    this.data = response["ucs_names"].map((uc) => {
      let index = indicators["uc_names"].indexOf(uc)
      if(index != -1){
        return { name: uc, m1:  indicators["indicadores"][index], show:true };
      } else {
        return { name: uc, m1:  -999999, show:true };
      }
      
    });
    this.items =  response["ucs_names"]
    function comparar(a, b) {
      if (a.m1 > b.m1) {
        return -1;
      }
      if (a.m1 < b.m1) {
        return 1;
      }
      // a deve ser igual a b
      return 0;
    }

    this.data = this.data.sort(comparar).map(item => {
      if(item.m1 == -999999 || item.m1 == -1){
        item.m1 = "Dados Insuficientes"
      }
      return item
    })
  },
};
</script>
<style scoped>

</style>