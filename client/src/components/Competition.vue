<template>
  <v-container fluid>

    <v-card offset-sm3>
      <v-alert
        v-model="alert"
        dismissible
        color="warning"
        icon="priority_high"
      >
        {{ alertMessage }}
      </v-alert>
      <v-card-title>
        <h2>{{ competition.name }}</h2>

        <v-spacer></v-spacer>
        <v-btn
          :to="{
            name: 'CompetitionEdit',
            params: {
                id: competition.id
            }
          }"
          color="primary">Edit</v-btn>
        <v-btn @click="deleteCompetition()" color="error">Delete</v-btn>

      </v-card-title>
      <div>
        Match Results (W-D-L): {{ competition.match_results }} <br/>

        <div v-if="competition.result">
          Results : {{ competition.result }}
        </div>

        <div v-if="competition.note">
          Note: {{ competition.note }}
        </div>
        <div v-if="competition.external_url">
            <a v-bind:href="competition.external_url">Competition's web site</a>
        </div>
        <v-spacer></v-spacer>

        <v-layout row>
          <h2>Matches</h2>
          <v-spacer></v-spacer>
          <v-btn color="success"
                :to="{name: 'MatchCreate'}">
            ADD MATCH
          </v-btn>
        </v-layout>
        <matches-table :matches="matches" :showOpponent="true"></matches-table>

        <h2>Player stats</h2>
        <player-matches-agg-table :player_matches="player_matches" :showPlayer="true"></player-matches-agg-table>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import API from '@/lib/API'
import MatchesTable from '@/components/MatchesTable'
import PlayerMatchesAggTable from '@/components/PlayerMatchesAggTable'

export default {
  components: {
    MatchesTable, PlayerMatchesAggTable
  },
  data () {
    return {
      alert: false,
      alertMessage: '',
      competition: {
        id: -1,
        name: null
      },
      matches: [],
      player_matches: []
    }
  },
  mounted () {
    const { id } = this.$route.params
    this.load(id)
  },
  methods: {
    load (id) {
      API.getCompetition(id)
        .then((competition) => {
          this.competition = competition
        })
      API.getMatchesByCompetition(id)
        .then((matches) => {
          this.matches = matches
        })
      API.getPlayerMatchesByCompetition(id)
        .then((player_matches) => {
          this.player_matches = player_matches
        })
    },
    deleteCompetition () {
      API.deleteCompetition(this.competition.id)
        .then(() => {
          this.$router.push({
            name: 'Competitions'
          })
        })
        .catch((err) => {
          this.alert = true
          this.alertMessage = err.response.data.error
        })
    }
  }
}
</script>
