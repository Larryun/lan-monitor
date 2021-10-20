<template>
  <div>
    <div class="row"> 
      <div class="timeslot online" style="width: 100px;"></div>
    </div>
    <div>{{ clients }}</div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: 'App',
  components: {
  },
  mounted() {
    this.fetchClients();
  },
  computed: {
    ...mapGetters({
      clients: "client/getClients"
    })
  },
  methods: {
    ...mapActions({
      "fetchClients": "client/fetchClients"
    })
  }
}
</script>

<style>

.online {
  background-color: green;
}

.timeslot {
  position: absolute;
  height: inherit;
}

.row {
  width: 100%;
  height: 60px;
  display: flex;
}
</style>
