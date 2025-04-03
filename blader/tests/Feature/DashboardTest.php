<?php

use App\Models\User;
use App\Models\Entry;

test('guests are redirected to the login page', function () {
    $this->get('/dashboard')->assertRedirect('/login');
});

test('authenticated users can visit the dashboard', function () {
    $this->actingAs($user = User::factory()->create());

    $this->get('/dashboard')
        ->assertStatus(200)
        ->assertSee('Latest Entries');
});

test('user sees latest entries section on dashboard', function () {
    $this->actingAs($user = User::factory()->create());

    $this->get('/dashboard')
        ->assertStatus(200)
        ->assertSee('Latest Entries')
        ->assertSee('No Entries Found')
        ->assertSee('Create One');
});

test('user sees latest entries on dashboard', function () {
    $this->actingAs($user = User::factory()->create());

    $entries = Entry::factory()->count(5)->create([
        'user_id' => $user->id,
    ]);

    $response = $this->get('/dashboard')
        ->assertStatus(200);

    foreach ($entries as $entry) {
        $response->assertSee($entry->slug)
            ->assertSee($entry->body)
            ->assertSee($entry->date_published);
    }
});
