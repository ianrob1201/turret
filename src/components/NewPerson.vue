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
        <td><div class="label">Pan</div></td>
        <td><input type="text" v-model="pan"/></td>
      </tr>
      <tr>
        <td><div class="label">Tilt</div></td>
        <td><input type="text" v-model="tilt"/></td>
      </tr>
      <tr>
        <td colspan="2"><div>Provide new user's details</div></td>
      </tr>
    </table>
  </div>
</template>

<script>
import PersonIcon from './PersonIcon.vue'
import { mapActions } from 'vuex'
import { peopleRef } from '../main'

export default {
  name: 'NewPerson',
  props: ['visible', 'newPerson', 'nextIndex'],
  data () {
    return {
      fullname: '',
      pan: "90",
      tilt: "90"
    }
  },
  components: {
    'personIcon': PersonIcon
  },
  methods: Object.assign({},
    mapActions(['stopEditing']),
    {
      add: function () {
        console.log(this)
        peopleRef.child(this.$options.propsData.nextIndex).set({
        // this.$router.app.$firebaseRefs.people.child('100').value({
          name: this.$data.fullname,
          pan: this.$data.pan,
          tilt: this.$data.tilt
        })
        console.log("ADDING2")
        console.log(this.$router.app.$firebaseRefs.people)
        this.stopEditing()
      },
      svg: function () {

      }
    }
  ),
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
