<script setup>
import { ref} from 'vue';
import FieldWorkForm from '@/components/Dialog/FieldWorkForm.vue';
import { useFieldWorkStore } from '@/stores/fieldwork.js'
import { Converter } from '@/functions/DateConverter'
import Navigation from '../components/Navigation.vue';

const dialog = ref(false)


// api call
const store = useFieldWorkStore()

// load before create phase
store.getFieldWorkList()
// show summary
const expand = ref(false)
// open/close ticket
const model = ref('no')
// show search
</script>

<template>
    <!-- navigation -->
    <Navigation/>
    <v-card color="grey-lighten-4" flat height="auto" rounded="0">
        <v-toolbar density="comfortable">

            <v-toolbar-title>Field Tickets</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-divider vertical></v-divider>


            <v-divider vertical></v-divider>
            <v-btn color="primary" @click="dialog = !dialog" prepend-icon="mdi-plus" class="mr-3">
                Tickets
                <FieldWorkForm :dialog="dialog" />
            </v-btn>
            <v-divider vertical></v-divider>

            <v-btn class="text-none" stacked>
                <v-badge content="2" color="error">
                    <v-icon>mdi-bell-outline</v-icon>
                </v-badge>
            </v-btn>
        </v-toolbar>
        <v-toolbar density="comfortable" class="mt-2">
            <v-sheet width="100%">
                <v-row align="center">
                    <v-col cols="6">
                        <v-text-field clearable placeholder="search here" label="search"></v-text-field>
                    </v-col>
                    <v-col cols="4">
                        <v-btn @click="store.completed()" class="bg-purple-darken-4 mr-2">closed</v-btn>
                        <v-btn @click="store.open()" class="bg-purple-darken-4">open</v-btn>
                    </v-col>
                </v-row>

            </v-sheet>
        </v-toolbar>
    </v-card>

    <!-- fieldwork data grid -->
    <v-infinite-scroll ref="infinite" height="500" side="end" @load="load">
        <v-container v-for="(item, index) in store.fieldworks" :key="index" v-if="store.fieldworks.length > 0">
            <v-card max-width="350" elevation="4">
                <v-card-item>
                    <v-card-title>
                        {{ item.task_name }}
                    </v-card-title>
                    <v-card-subtitle>
                        <v-row>
                            <v-col cols="auto">
                                {{ item.assignee }}
                            </v-col>
                            <v-divider vertical></v-divider>
                            <v-col cols="auto">
                                {{ Converter(item.date) }}
                            </v-col>
                            <v-col cols="auto">
                                status
                                <v-icon icon="mdi-circle-small" size="x-large" color="green-darken-2"></v-icon>
                            </v-col>
                        </v-row>
                    </v-card-subtitle>

                    <v-card-actions>
                        <v-btn @click="expand = !expand" class="bg-purple-accent-3"
                            :append-icon="expand ? 'mdi-chevron-up' : 'mdi-chevron-down'">
                            {{ !expand ? 'Read more' : 'Read less' }}
                        </v-btn>
                    </v-card-actions>

                    <v-expand-transition>
                        <div class="summary" v-show="expand">
                            <v-card-text>
                                {{ item.activities }}
                                <v-row>
                                    <v-col cols="auto">

                                        <v-switch v-model="model" hide-details true-value="closed" false-value="open" initial-value="open"
                                            color="green" :label="`${model}`"></v-switch>
                                    </v-col>
                                </v-row>
                            </v-card-text>

                        </div>
                    </v-expand-transition>
                </v-card-item>
            </v-card>
        </v-container>
        <v-container v-else>
            <h3>Hoorah! no Fieldwork Tickets</h3>

        </v-container>
    </v-infinite-scroll>
</template>