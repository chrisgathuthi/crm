<script setup>
const props = defineProps(["dialog"])
console.log(props.dialog)

</script>
<template>
    <v-row justify="center">
        <v-dialog persistent width="1024" v-model="props.dialog">
            <v-card>
                <v-card-title>
                    <span class="text-h5">Ticket Form</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12">
                                <v-text-field label="Task Name*" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                                <v-text-field label="Location*" required></v-text-field>
                            </v-col>
                            <v-container fluid>
                                <v-textarea clearable clear-icon="mdi-close-circle" label="Activites*"
                                    model-value="1. "></v-textarea>
                            </v-container>
                            <v-col cols="12">
                                <v-select :items="['John Doe', 'Jane Doe', 'Tim Marshall']" label="Assignee*" required></v-select>
                            </v-col>

                        </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                        Close
                    </v-btn>
                    <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
                        Save
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>