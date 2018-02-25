<template>
  <div class="hello">
    <button v-on:click="login()">Login</button>
    <table>
      <tr>
        <th>Person</th>
        <th>Pan Angle</th>
        <th>Tilt Angle</th>
      </tr>
      <tr v-for="person in people" v-bind:key="person['.key']">
        <template v-if="!editingPerson(person)">
          <td v-on:click="edit(person)">{{ person.name }}</td>
          <td v-on:click="edit(person)">{{ person.pan }}</td>
          <td v-on:click="edit(person)">{{ person.tilt }}</td>
          <td><button class="shoot" v-on:click="shoot(person)">Shoot</button></td>
          <td><button class="aim" v-on:click="aim(person)">Aim</button></td>
          <td><button class="remove" v-on:click="deletePerson(person)">Remove</button></td>
        </template>
        <template v-else>
          <td><input type="text" v-on:keyup.enter="saveEdit(person)" v-on:blur="saveEdit(person)" v-model="person.name"/></td>
          <td><input type="text" v-on:keyup.enter="saveEdit(person)" v-on:blur="saveEdit(person)" v-model="person.pan"/></td>
          <td><input type="text" v-on:keyup.enter="saveEdit(person)" v-on:blur="saveEdit(person)" v-model="person.tilt"/></td>
        </template>
      </tr>
      <tr>
        <td colspan='2'><button @click="startEditing">Add New</button></td>
      </tr>
    </table>
    <newPerson v-if="isEditing" v-bind:nextIndex="nextIndex"/>
    <div id="manualCommand">
      <div>Manual Command</div>
      <input type="text" v-model="customCommandText" v-on:keyup.enter="customCommand()"/>
      <button class="shoot" v-on:click="customCommand()">Execute</button>
    </div>
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
      editRotation: 0,
      customCommandText: ''
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
  computed: Object.assign({},
    mapGetters(['isEditing']),
    {
      nextIndex: function () {
        return this.$data.people.length
      }
    }),
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
          return {name: person.name, pan: person.pan, tilt: person.tilt}
        })
        console.log("PEOPLE")
        console.log(firebasePeople)
        this.$firebaseRefs.people.set(firebasePeople)
        this.$data.editing = null
      },
      deletePerson: function (person) {
        this.$firebaseRefs.people.child(person['.key']).remove()
      },
      shoot: function (person) {
        Vue.http.post('https://cyormhgc0l.execute-api.eu-west-1.amazonaws.com/prod/',
          {name: person.name, command: 'SHOOT'},
          {headers: {
            'x-api-key': 'tIIVFTUPA89L8Roz46CBL4vnCW4BWKcQ6pkvvvmY',
            'Content-Type': 'application/json'
          }}
        ).then(response => {
          console.log('It only went and worked!!')
          console.log(response)
        })
      },
      aim: function (person) {
        Vue.http.post('https://cyormhgc0l.execute-api.eu-west-1.amazonaws.com/prod/',
          {name: person.name, command: 'AIM'},
          {headers: {
            'x-api-key': 'tIIVFTUPA89L8Roz46CBL4vnCW4BWKcQ6pkvvvmY',
            'Content-Type': 'application/json'
          }}
        ).then(response => {
          console.log('It only went and worked!!')
          console.log(response)
        })
      },
      customCommand: function () {
        Vue.http.post('https://cyormhgc0l.execute-api.eu-west-1.amazonaws.com/prod/',
          {customCommand: this.$data.customCommandText, command: 'CUSTOM'},
          {headers: {
            'x-api-key': 'tIIVFTUPA89L8Roz46CBL4vnCW4BWKcQ6pkvvvmY',
            'Content-Type': 'application/json'
          }}
        )
        this.$data.customCommandText = ''
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
.aim {
  background-color: #ee7700;
}
</style>
