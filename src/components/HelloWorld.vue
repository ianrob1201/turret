<template>
  <div class="hello">
    <button v-on:click="login()">Login</button>
    <table>
      <tr>
        <th>Person</th>
        <th>Rotation</th>
      </tr>
      <tr v-for="person in people" v-bind:key="person['.key']">
        <template v-if="!editingPerson(person)">
          <td v-on:click="edit(person)">{{ person.name }}</td>
          <td v-on:click="edit(person)">{{ person.rotation }}</td>
          <td><button class="shoot" v-on:click="shoot(person)">Shoot</button></td>
          <td><button class="remove" v-on:click="deletePerson(person)">Remove</button></td>
        </template>
        <template v-else>
          <td><input type="text" v-on:keyup.enter="saveEdit(person)" v-on:blur="saveEdit(person)" v-model="person.name"/></td>
          <td><input type="text" v-on:keyup.enter="saveEdit(person)" v-on:blur="saveEdit(person)" v-model="person.rotation"/></td>
        </template>
      </tr>
      <tr>
        <td colspan='2'><button @click="startEditing">Add New</button></td>
      </tr>
    </table>
    <newPerson v-if="isEditing"/>
  </div>
</template>

<script>
import Vue from 'vue'
import { db } from '../main'
import firebase from 'firebase'
import NewPerson from './NewPerson.vue'
import { mapGetters, mapActions } from 'vuex'

console.log(mapActions(['startEditing']))
export default {
  name: 'HelloWorld',
  data () {
    return {
      people: [],
      editing: null,
      addingNew: false,
      editRotation: 0
    }
  },
  firebase () {
    return {
      people: db.ref('people')
    }
  },
  components: {
    'newPerson': NewPerson
  },
  computed: mapGetters([
    'isEditing'
  ]),
  methods: Object.assign({},
    mapActions(['startEditing']),
    {
      connect: function (event) {
        this.$router.app.$firebaseRefs.anArray.push({
          text: 'hello'
        })
      },
      login: function (event) {
        var provider = new firebase.auth.GoogleAuthProvider()
        firebase.auth().signInWithPopup(provider).then(function (result) {
          // Can access google token from here if needed
        }).catch(function (error) {
          // Can do something about the error here
          console.log(error)
        })
      },
      edit: function (person) {
        this.$data.editing = person['.key']
      },
      editingPerson: function (person) {
        return person['.key'] === this.$data.editing
      },
      saveEdit: function (person) {
        const firebasePeople = this.$data.people.map(function (person) {
          return {name: person.name, rotation: person.rotation}
        })
        this.$firebaseRefs.people.set(firebasePeople)
        this.$data.editing = null
      },
      showNew: function () {
        this.$firebaseRefs.people.push({
          name: 'newPerson',
          rotation: 0
        })
      },
      deletePerson: function (person) {
        this.$firebaseRefs.people.child(person['.key']).remove()
      },
      shoot: function (person) {
        Vue.http.post('https://cyormhgc0l.execute-api.eu-west-1.amazonaws.com/prod/',
          {name: person.name},
          {headers: {
            'x-api-key': 'tIIVFTUPA89L8Roz46CBL4vnCW4BWKcQ6pkvvvmY',
            'Content-Type': 'application/json'
          }}
        ).then(response => {
          console.log('It only went and worked!!')
          console.log(response)
        })
      }
    }
  )
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.remove {
  background-color: #ee4422;
}
.shoot {
  background-color: #44ee22;
}
</style>
