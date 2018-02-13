import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  editing: false
}

const mutations = {
  startEditing (state) {
    state.editing = true
  },
  stopEditing (state) {
  	state.editing = false
  }
}

const actions = {
  startEditing: ({ commit }) => commit('startEditing'),
  stopEditing: ({ commit }) => commit('stopEditing')
}

const getters = {
  isEditing: state => state.editing
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})