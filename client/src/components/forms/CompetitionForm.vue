<template>
  <v-layout>
    <v-flex xs12>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
        v-model="competition.name"
        :rules="nameRules"
        :counter="30"
        label="Name"
        required
        ></v-text-field>
        <v-text-field
        v-model="competition.result"
        label="Result"
        ></v-text-field>
        <v-textarea
        v-model="competition.note"
        label="Note"
        ></v-textarea>
        <v-text-field
        v-model="competition.external_url"
        label="Competition URL"
        ></v-text-field>

        <v-btn :disabled="!valid" @click="submit">submit</v-btn>
        <v-btn @click="clear">clear</v-btn>
      </v-form>
    </v-flex>
  </v-layout>

</template>

<script>

export default {
  props: ['competition', 'onSubmit'],
  data: () => ({
    valid: true,
    nameRules: [
      v => (v && v.trim().length !== 0) || 'Name is required yo',
      v => !!v || 'Name is required',
      v => (v && v.length <= 30) || 'Name must be less than 40 characters'
    ]
  }),
  methods: {
    submit () {
      if (this.valid) {
        this.onSubmit()
      }
    },
    clear () {
      this.$refs.form.reset()
    }
  }
}
</script>
