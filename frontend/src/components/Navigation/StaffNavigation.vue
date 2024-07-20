<template>
    <v-app-bar>
        <v-toolbar prominent class="bg-grey-lighten-5 static" tag="div">
            <v-toolbar-title>Staff</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn >
                Active Tickets
                <v-badge color="error" dot>
                    <v-icon>mdi mdi-hard-hat</v-icon>
                </v-badge>
            </v-btn>
            <v-btn prepend-icon="mdi mdi-timeline-text-outline">Ticket History</v-btn>
        </v-toolbar>
    </v-app-bar>
</template>