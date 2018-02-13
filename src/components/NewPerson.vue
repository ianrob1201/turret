<template>
  <div id="all">
    <table>
      <tr>
        <td><div class="label">Full name</div></td>
        <td><input type="text" v-model="fullname"/></td>
        <td rowspan="3"><button id="add" v-on:click="add">Add</button></td>
        <td rowspan="3"><personIcon v-bind:initials="initials" v-if="initials"/></td>
      </tr>
      <tr>
        <td><div class="label">Rotation</div></td>
        <td><input type="text" v-model="rotation"/></td>
      </tr>
      <tr>
        <td colspan="2"><div>Provide new user's details</div></td>
      </tr>
    </table>
    
  </div>
</template>

<script>
import PersonIcon from './PersonIcon.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'NewPerson',
  props: ['visible', 'newPerson'],
  data () {
    return {
      fullname: '',
      rotation: 0
    }
  },
  components: {
    'personIcon': PersonIcon
  },
  methods: Object.assign({}, 
    mapActions(['stopEditing']),
    {
    add: function () {
      this.$router.app.$firebaseRefs.people.push({
        name: this.$data.fullname,
        rotation: this.$data.rotation
      })
      this.stopEditing()
    },
    svg: function () {

    }
  }),
  computed: {
    initials: function () {
      return this.$data.fullname.split(' ').map(x => x.charAt(0)).join('').toUpperCase()
    }
  }
}
</script>

<style scoped>
  #all {
    /*background-color: orange;*/
    width: fit-content;
  }

  #add {
    height: 100%;
    display: inline-block;
  }

  .label {
    display: inline;
  }

  .labelInput {
    display: inline;
  }
</style>
