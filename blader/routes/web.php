<?php

use App\Livewire\Settings\Appearance;
use App\Livewire\Settings\Password;
use App\Livewire\Settings\Profile;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\EntryController;

Route::get('/', function () {
    return view('welcome');
})->name('home');

Route::get('dashboard', [DashboardController::class, 'index'])
    ->middleware(['auth', 'verified'])
    ->name('dashboard');

Route::middleware(['auth'])->group(function () {
    Route::redirect('settings', 'settings/profile');

    Route::get('settings/profile', Profile::class)->name('settings.profile');
    Route::get('settings/password', Password::class)->name('settings.password');
    Route::get('settings/appearance', Appearance::class)->name('settings.appearance');
});

require __DIR__.'/auth.php';

Route::get('/entries', [EntryController::class, 'index'])
    ->middleware(['auth', 'verified'])
    ->name('entries.index');

Route::get('/entries/create', [EntryController::class, 'create'])
    ->middleware(['auth', 'verified'])
    ->name('entries.create');

Route::post('/entries/store', [EntryController::class, 'store'])
    ->middleware(['auth', 'verified'])
    ->name('entries.store');

Route::get('/entries/{slug}', [EntryController::class, 'show'])
    ->middleware(['auth', 'verified'])
    ->name('entries.show');

Route::get('/entries/edit/{slug}', [EntryController::class, 'edit'])
    ->middleware(['auth', 'verified'])
    ->name('entries.edit');

Route::delete('/entries/{slug}', [EntryController::class, 'destroy'])
    ->middleware(['auth', 'verified'])
    ->name('entries.destroy');
